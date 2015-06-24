import numpy as np
import networkx as nx
from multiplex import MultiplexConnectome
import json
import community

sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

data_root = '/home/cbarnes/data/connectomes'

G = C['ww'].collapse('GapJunction', 'Synapse')


def optimise_Q(s, B_sym):
    """
    Fine-tunes binary partitioning. Slow.

    :param s: vector of -1 and 1 for two partitions
    :param B_sym: B + B.T, the symmetricalised modularity matrix (in np.mat form)
    :return: (optimised_s, best_Q)
    """
    m = np.shape(B_sym)[0]
    Q = float(1/(4*m) * s.T * np.mat(B_sym) * s)
    ret_s = np.array(s)

    while True:
        best_el = None
        for el in range(len(s)):
            working_s = np.copy(ret_s)
            working_s[el] *= -1
            new_Q = float(1/(4*m) * np.mat(working_s).T * B_sym * np.mat(working_s))
            if new_Q > Q:
                Q = new_Q
                best_el = el
        if best_el is None:
            break
        else:
            ret_s[best_el] *= -1

    return ret_s, Q


def graph_to_partitions_and_Q(G, optimise_partitions=True):
    nodelist = sorted(G.nodes())

    A = nx.to_numpy_matrix(G, nodelist=nodelist, weight=None)  # adjacency matrix
    G_ints = nx.convert_node_labels_to_integers(G, ordering='sorted', label_attribute='name')
    in_degree_dict = G_ints.in_degree()
    out_degree_dict = G_ints.out_degree()
    m = G.number_of_edges()  # number of edges

    if m == 0:
        return (G.nodes(), []), 0

    make_B = np.vectorize(
        lambda i, j: (in_degree_dict[int(i)]*out_degree_dict[int(j)])/m,
        otypes=[np.dtype('float64')]
    )

    B = A - np.fromfunction(make_B, A.shape)
    B_sym = B + B.T

    eigvals, eigvecs = np.linalg.eig(B_sym)
    max_eigvec = eigvecs[:, np.where(eigvals == np.max(eigvals))]

    s = np.ones(max_eigvec.shape)
    s[max_eigvec < 0] = -1

    if optimise_partitions:
        s, Q = optimise_Q(s, np.mat(B_sym))
    else:
        Q = float(1/(4*m) * np.mat(s).T * np.mat(B_sym) * np.mat(s))

    neg = []
    pos = []

    for node_id, partition in enumerate(s):
        if partition < 0:
            neg.append(nodelist[node_id])
        else:
            pos.append(nodelist[node_id])

    return (neg, pos), Q


def modularise(G):

    (neg, pos), Q = graph_to_partitions_and_Q(G)
    data = {'partitions': (neg, pos), 'Q': Q}
    if len(neg) > 0 and len(pos) > 0:
        data['children'] = (modularise(G.subgraph(neg)), modularise(G.subgraph(pos)))
    return data


def opt_modularise(G, force_partition=False, minor_optimise=True):
    (neg, pos), Q = graph_to_partitions_and_Q(G, minor_optimise)
    if Q <= 0.0001 and not force_partition:
        return {'partitions': ([], G.nodes()), 'Q': Q, 'children': None}
    data = {'partitions': (neg, pos), 'Q': Q}
    if len(neg) > 0 and len(pos) > 0:
        data['children'] = (
            opt_modularise(G.subgraph(neg), minor_optimise=minor_optimise),
            opt_modularise(G.subgraph(pos), minor_optimise=minor_optimise)
        )
    return data


def get_modules(mods):
    modules = []
    if mods['children']:
        for mod in mods['children']:
            modules.extend(get_modules(mod))
    else:
        modules.extend(mods['partitions'])

    return [module for module in modules if module]

# mods = modularise(G)
# json.dump(mods, open('mods.json', 'w'), indent=2, sort_keys=True)

mods = opt_modularise(G, True)
# json.dump(mods, open('opt_mods2.json', 'w'), indent=2, sort_keys=True)
modules = get_modules(mods)
print('done')