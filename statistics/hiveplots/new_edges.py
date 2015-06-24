import networkx as nx
from multiplex import MultiplexConnectome
import json
from hiveplotter import HivePlot
from collections import defaultdict

morphology_path = '/home/cbarnes/data/connectome/morphologies.json'

mode = 'ww-ac'
split = True
order_by = 'AP'

C = dict()
phys = dict()

for source in ('ww', 'ac'):
    network_path = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'.format(source)
    G = nx.read_gpickle(network_path)

    if order_by == 'AP':
        morph = json.load(open(morphology_path, 'r'))

        for node, data in G.nodes_iter(data=True):
            data['soma_position'] = morph[node]['soma']
            data['AP'] = - morph[node]['soma'][1]

    C[source] = MultiplexConnectome(G)
    phys[source] = C[source].compose('GapJunction', 'Synapse')

G_diff = nx.MultiDiGraph()
G_diff.add_nodes_from(C['ww'].whole.nodes(data=True))

for source in ('ww', 'ac'):
    for etype in ('GapJunction', 'Synapse'):
        assert C[source][etype].number_of_edges() == nx.DiGraph(C[source][etype]).number_of_edges()

edgesets = defaultdict(dict)
for etype in ('GapJunction', 'Synapse'):

    edgesets['ac'][etype] = set(C['ac'][etype].edges_iter())
    assert len(edgesets['ac'][etype]) == len(C['ac'][etype].edges())

    edgesets['ww'][etype] = set(C['ww'][etype].edges_iter())
    assert len(edgesets['ww'][etype]) == len(C['ww'][etype].edges())

    edgesets['ww-ac'][etype] = edgesets['ww'][etype] - edgesets['ac'][etype]
    edgesets['ac-ww'][etype] = edgesets['ac'][etype] - edgesets['ww'][etype]

    for src, tgt in edgesets[mode][etype]:
        G_diff.add_edge(src, tgt, attr_dict=C[mode[:2]][etype].edge[src][tgt][0])

# assert G_diff.number_of_edges() == phys['ww'].number_of_edges() - phys['ac'].number_of_edges()

def edge_to_str(edge):
    return '({}, {}, {})'.format(edge[0], edge[1], json.dumps(edge[2], sort_keys=True))


def_args = {
                'node_class_attribute': 'type',
                'node_class_values': ['interneuron', 'motor', 'sensory'],
                'order_nodes_by': order_by,
                'edge_alpha': 0.2,
                'label_size': 14,
                'edge_thickness_range': (0.003, 0.003),
                'node_size_range': (0.08, 0.16),
                'split_axes': ['interneuron', 'motor', 'sensory'] if split else []
            }


H = HivePlot(G_diff,
                 edge_colour_attribute="type", edge_category_legend=True,
                 edge_category_colours={'Synapse': 'Cyan', 'GapJunction': 'Yellow'}, **def_args)
H.draw(save_path='img/new_edges/{}_{}_{}split.pdf'.format(mode, order_by, '' if split else 'no'))

H = HivePlot(phys['ac'],
                 edge_colour_attribute="type", edge_category_legend=True,
                 edge_category_colours={'Synapse': 'Cyan', 'GapJunction': 'Yellow'}, **def_args)
H.draw(save_path='img/new_edges/{}_{}_{}split.pdf'.format('ac', order_by, '' if split else 'no'))

H = HivePlot(phys['ww'],
                 edge_colour_attribute="type", edge_category_legend=True,
                 edge_category_colours={'Synapse': 'Cyan', 'GapJunction': 'Yellow'}, **def_args)
H.draw(save_path='img/new_edges/{}_{}_{}split.pdf'.format('ww', order_by, '' if split else 'no'))

print('done')