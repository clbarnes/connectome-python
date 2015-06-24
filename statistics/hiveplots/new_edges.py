import networkx as nx
from multiplex import MultiplexConnectome
import json

C = dict()
phys = dict()

for source in ('ww', 'ac'):
    network_path = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'.format(source)
    C[source] = MultiplexConnectome(nx.read_gpickle(network_path))
    phys[source] = C[source].compose('GapJunction', 'Synapse')

G_diff = nx.MultiDiGraph()

for src, tgt, data in phys['ww'].edges_iter(data=True):
    etype = data['type']

    try:
        assert tgt in C['ac'][etype].edge[src]
    except (KeyError, AssertionError):
        G_diff.add_edge(src, tgt, attr_dict=data)

def edge_to_str(edge):
    return '({}, {}, {})'.format(edge[0], edge[1], json.dumps(edge[2], sort_keys=True))

full_edgeset = {edge_to_str(edge) for edge in C['ac']['GapJunction'].edges_iter(data=True)}\
               | {edge_to_str(edge) for edge in C['ac']['Synapse'].edges_iter(data=True)}

small_edgeset = {edge_to_str(edge) for edge in phys['ac'].edges_iter(data=True)}


print('done')