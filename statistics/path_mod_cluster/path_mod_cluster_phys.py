from path_mod_cluster.shared import iterate_adj_mats, av_path_length
# from shared import av_path_length
from multiplex import MultiplexConnectome
import networkx as nx
import os
import numpy as np
import json
from scipy import io as sio
import community
import progressbar as pb


def zscore(val, mean, sd):
    return (val - mean)/sd


def iterate_adj_mats(path):
    data = sio.loadmat(path)
    var_name_stub = '{}_whole_'.format('ww' if '/ww/' in path else 'ac')
    node_mapping = {i: node for i, node in enumerate(data['nodelist'])}
    for var_name in (var_name_stub + str(i) for i in range(1000)):
        G = nx.from_numpy_matrix(data[var_name])
        yield nx.relabel_nodes(G, node_mapping)


sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

data_root = '/home/cbarnes/data/connectomes'
output = dict()

pbar = pb.ProgressBar(maxval=1001*2, widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()
count = 0
for source, connectome in C.items():
    output[source] = dict()

    G = nx.DiGraph(connectome.compose('Synapse', 'GapJunction'))

    output[source]['path_length'] = dict()
    output[source]['path_length']['actual'] = av_path_length(G)
    output[source]['transitivity'] = dict()
    output[source]['transitivity']['actual'] = nx.transitivity(G)
    G_undi = nx.Graph(G)
    part = community.best_partition(G_undi)
    output[source]['maximum_modularity'] = dict()
    output[source]['maximum_modularity']['actual'] = community.modularity(part, G_undi)
    output[source]['clustering'] = dict()
    output[source]['clustering']['actual'] = nx.average_clustering(G_undi)
    count += 1
    pbar.update(count)

    path_lengths = []
    transitivities = []
    modularities = []
    clusterings = []

    for G in iterate_adj_mats(os.path.join(data_root, 'randoms_phys', source, 'whole.mat')):
        path_lengths.append(av_path_length(G))
        transitivities.append(nx.transitivity(G))
        clusterings.append(nx.average_clustering(G))
        G_undi = nx.Graph(G)
        part = community.best_partition(G_undi)
        modularities.append(community.modularity(part, G_undi))
        clusterings.append(nx.average_clustering(G_undi))
        count += 1
        pbar.update(count)

    output[source]['path_length']['control_mean'] = np.mean(path_lengths)
    output[source]['path_length']['control_sd'] = np.std(path_lengths)

    output[source]['transitivity']['control_mean'] = np.mean(transitivities)
    output[source]['transitivity']['control_sd'] = np.std(transitivities)

    output[source]['maximum_modularity']['control_mean'] = np.mean(modularities)
    output[source]['maximum_modularity']['control_sd'] = np.std(modularities)

    output[source]['clustering']['control_mean'] = np.mean(clusterings)
    output[source]['clustering']['control_sd'] = np.std(clusterings)

for source, source_dict in output.items():
    for measure, measure_dict in source_dict.items():
        measure_dict['actual_z'] = zscore(measure_dict['actual'], measure_dict['control_mean'], measure_dict['control_sd'])

json.dump(output, open('path_cluster_phys_output.json', 'w'), sort_keys=True, indent=4)


print('done')