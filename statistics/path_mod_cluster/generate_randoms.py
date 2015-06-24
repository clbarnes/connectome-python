from shared import order, connectomes
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

# pbar = pb.ProgressBar(widgets=['Generating: ', pb.Percentage(), ' ', pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()],
#                       maxval=len(order)*(len(d['ww'].sub)+2)).start()

count = 0

q = Queue(maxsize=5)
proc = Process(target=worker, args=(q,))
proc.daemon = True
proc.start()


for network_id in order:

    # os.makedirs(os.path.join(root_dir, network_id, 'layers'), exist_ok=True)
    os.makedirs(os.path.join(root_dir + '_phys', network_id), exist_ok=True)

    nodelist = sorted(d[network_id].whole.nodes())
    #
    # for layer, graph in d[network_id].sub.items():
    #     filename = os.path.join(root_dir, network_id, 'layers', '{}.mat'.format(layer))
    #     G = nx.DiGraph(graph) if layer != 'GapJunction' else nx.Graph(graph)
    #     for_mat = {'{}_{}_{}'.format(network_id, layer, i): this_graph
    #             for i, this_graph in enumerate(parallel_randomise(G))}
    #     for_mat['nodelist'] = np.array(nodelist)
    #     for_mat['filename'] = filename
    #     for_mat['layer'] = layer
    #     for_mat['{}_{}_{}'.format(network_id, layer, 'source')] = nx.to_numpy_matrix(G, nodelist=nodelist)
    #     q.put(for_mat)
    #     count += 1
    #     pbar.update(count)
    #
    # filename = os.path.join(root_dir, network_id, 'whole.mat')
    # G = nx.DiGraph(d[network_id].whole)
    # for_mat = {'{}_whole_{}'.format(network_id, i): this_graph
    #             for i, this_graph in enumerate(parallel_randomise(G))}
    # for_mat['nodelist'] = np.array(nodelist)
    # for_mat['filename'] = filename
    # for_mat['{}_{}_{}'.format(network_id, 'whole', 'source')] = nx.to_numpy_matrix(G, nodelist=nodelist)
    # q.put(for_mat)
    # count += 1
    # pbar.update(count)
    #
    # filename = os.path.join(root_dir + '_no-np', network_id, 'whole.mat')
    # G = nx.DiGraph(d[network_id].compose('GapJunction', 'Monoamine', 'Synapse'))
    # for_mat = {'{}_whole_{}'.format(network_id, i): this_graph
    #             for i, this_graph in enumerate(parallel_randomise(G))}
    # for_mat['nodelist'] = np.array(nodelist)
    # for_mat['filename'] = filename
    # for_mat['{}_{}_{}'.format(network_id, 'whole', 'source')] = nx.to_numpy_matrix(G, nodelist=nodelist)
    # q.put(for_mat)
    # count += 1
    # pbar.update(count)

    filename = os.path.join(root_dir + '_phys', network_id, 'whole.mat')
    G = nx.DiGraph(d[network_id].compose('GapJunction', 'Synapse'))
    for_mat = {'{}_whole_{}'.format(network_id, i): this_graph
                for i, this_graph in enumerate(parallel_randomise(G))}
    for_mat['nodelist'] = np.array(nodelist)
    for_mat['filename'] = filename
    for_mat['{}_{}_{}'.format(network_id, 'whole', 'source')] = nx.to_numpy_matrix(G, nodelist=nodelist)
    save_to_mat(for_mat)
    # q.put(for_mat)

q.close()
q.join_thread()

print('done')