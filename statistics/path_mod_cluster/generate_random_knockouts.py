from shared import order, connectomes, to_binarised_adj, clean_graph
import connectome_utils as utl
import networkx as nx
import numpy as np
from scipy import io as sio
import os
from multiprocessing import Pool, cpu_count, Queue, Process
import progressbar as pb


def parallel_randomise(graph, reps=1000):
    graph_copies = (graph for _ in range(reps))
    with Pool(cpu_count()) as p:
        out = p.map(graph_to_randomised_adj, graph_copies, chunksize=50)

    return out


def graph_to_randomised_adj(graph):
    G = utl.randomise(graph, keep_labels=True)
    return nx.to_numpy_matrix(G, nodelist=sorted(G.nodes_iter()))


def save_to_mat(d):
    sio.savemat(d['filename'], d)


def worker(q):
    while True:
        item = q.get()
        save_to_mat(item)

d = dict(zip(order, connectomes))

physical_n = ['GapJunction', 'Synapse']
extrasyn_n = ['Monoamine', 'Neuropeptide']

root_dir = '/home/cbarnes/data/connectomes/randoms'

to_knock_out = {'transmitters': set(), 'receptors': set()}

for _1, _2, data in d['ww'].whole.edges_iter(data=True):
    if data['type'] == 'Neuropeptide':
        to_knock_out['transmitters'].add(data.get('transmitter', None))
        to_knock_out['receptors'].add(data.get('receptor', None))

for st in to_knock_out.values():
    if None in st:
        st.remove(None)

pbar = pb.ProgressBar(widgets=['Generating: ', pb.Percentage(), ' ', pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()],
                      maxval=2*(len(to_knock_out['transmitters']) + len(to_knock_out['receptors']))).start()

count = 0

q = Queue(maxsize=1)
proc = Process(target=worker, args=(q,))
proc.daemon = True
proc.start()

for network_id in order:

    os.makedirs(os.path.join(root_dir, network_id), exist_ok=True)
    os.makedirs(os.path.join(root_dir, network_id, 'transmitter_ko'), exist_ok=True)
    os.makedirs(os.path.join(root_dir, network_id, 'receptor_ko'), exist_ok=True)

    G = d[network_id].whole

    for node, data in G.nodes(data=True):
        data = data.clear()
    for src, tgt, data in G.edges(data=True):
        data = data.clear()

    nodelist = sorted(G.nodes())

    source_data = {'nodelist': np.array(nodelist),
                   'adjacency': to_binarised_adj(G),
                   'filename': os.path.join(root_dir, network_id, 'source_data.mat')}
    # q.put(source_data)

    for transmitter in to_knock_out['transmitters']:
        filename = os.path.join(root_dir, network_id, 'transmitter_ko', 'transmitter_ko_{}.mat'.format(transmitter))
        knocked_out = clean_graph(utl.knockout(G, transmitter=transmitter))
        transmitter_name = transmitter.replace('-', '')
        randoms = parallel_randomise(knocked_out)
        for_mat = {'{}_transmitter_ko_{}_{}'.format(network_id, transmitter_name, i): this_graph
                for i, this_graph in enumerate(randoms)}
        for_mat['nodelist'] = np.array(nodelist)
        for_mat['filename'] = filename
        for_mat['knockout_type'] = 'transmitter'
        for_mat['knockout'] = transmitter_name
        for_mat['{}_transmitter_ko_{}_{}'.format(network_id, transmitter_name, 'source')] = to_binarised_adj(knocked_out)
        q.put(for_mat)
        count += 1
        pbar.update(count)

    for receptor in to_knock_out['receptors']:
        filename = os.path.join(root_dir, network_id, 'receptor_ko', 'receptor_ko_{}.mat'.format(receptor))
        knocked_out = clean_graph(utl.knockout(G, receptor=receptor))
        receptor_name = receptor.replace('-', '')
        randoms = parallel_randomise(knocked_out)
        for_mat = {'{}_receptor_ko_{}_{}'.format(network_id, receptor_name, i): this_graph
                for i, this_graph in enumerate(randoms)}
        for_mat['nodelist'] = np.array(nodelist)
        for_mat['filename'] = filename
        for_mat['knockout_type'] = 'receptor'
        for_mat['knockout'] = receptor_name
        for_mat['{}_transmitter_ko_{}_{}'.format(network_id, receptor_name, 'source')] = to_binarised_adj(knocked_out)
        q.put(for_mat)
        count += 1
        pbar.update(count)

q.close()
q.join_thread()

print('done')