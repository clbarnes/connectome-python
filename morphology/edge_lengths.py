import numpy as np
from scipy.spatial.distance import cdist
import json
import networkx as nx
from multiplex import MultiplexConnectome

node_morphs = json.load(open('morphologies.json', 'r'))

ma = MultiplexConnectome(nx.read_gpickle('/home/cbarnes/data/connectome/networks/ac_complete.gpickle'))['Monoamine']


def get_min_dist(src, tgt):
    src_data = np.array(node_morphs[src]['neurone'])
    tgt_data = np.array(node_morphs[tgt]['neurone'])

    dist_mat = cdist(src_data[:, :3], tgt_data[:, :3])

    raw_min_dist = np.min(dist_mat)

    src_ind, tgt_ind = np.unravel_index(np.argmin(dist_mat), dist_mat.shape)

    return max(raw_min_dist - src_data[src_ind, 3]/2 - tgt_data[tgt_ind, 3]/2, 0)


def make_dist_mat_and_graph():
    nodelist = sorted(ma.nodes_iter())

    # distance matrix
    make_dist = np.vectorize(
        lambda i, j: get_min_dist(nodelist[int(i)], nodelist[int(j)]),
        otypes=[np.dtype('float64')]
    )

    dist = np.fromfunction(make_dist, (len(nodelist), len(nodelist)))

    np.savetxt('dist_mat.csv', dist, delimiter=',')
    nodemapping = dict(enumerate(nodelist))
    with open('nodelist.txt', 'w') as f:
        f.write('\n'.join(nodelist))

    # nx graph
    G = nx.from_numpy_matrix(dist)
    comp = nx.complement(G)
    complete = nx.compose(G, comp)
    nx.relabel_nodes(G, nodemapping, False)

    for src, tgt, data in complete.edges_iter(data=True):
        data['distance'] = data.pop('weight', 0)

    nx.write_gpickle(complete, 'minimum_distance.gpickle')

make_dist_mat_and_graph()

print('done')