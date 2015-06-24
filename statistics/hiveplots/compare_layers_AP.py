import networkx as nx
from multiplex import MultiplexConnectome
from hiveplotter import HivePlot
import json
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


morphology_path = '/home/cbarnes/data/connectome/morphologies.json'
morph = json.load(open(morphology_path, 'r'))

for source in ('ww', 'ac'):
    network_path = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'.format(source)
    G = nx.read_gpickle(network_path)

    for order_by in ('AP', 'degree'):

        if order_by == 'AP':
            for node, data in G.nodes_iter(data=True):
                data['soma_position'] = morph[node]['soma']
                data['AP'] = - morph[node]['soma'][1]

        for split in (True, False):

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

            C = MultiplexConnectome(G)

            for etype in ('GapJunction', 'Synapse'):
                H = HivePlot(C[etype],
                             edge_colour_attribute="weight", **def_args)
                H.draw(save_path='img/compare_layers_{}/{}_{}_{}_{}split.pdf'.format(order_by, source, etype, order_by, '' if split else 'no'))

            H = HivePlot(C['Monoamine'],
                             edge_colour_attribute="transmitter", edge_category_legend=True,
                             edge_colour_gradient='Rainbow', **def_args)
            H.draw(save_path='img/compare_layers_{}/{}_{}_{}_{}split.pdf'.format(order_by, source, 'Monoamine', order_by, '' if split else 'no'))

            # H = HivePlot(C['Neuropeptide'],
            #                  edge_colour_attribute="receptor", edge_category_legend=True,
            #                  edge_colour_gradient='Rainbow', **def_args)
            # H.draw(save_path='img/compare_layers_{}/{}_{}_{}_{}split.pdf'.format(order_by, source, 'Neuropeptide', order_by, '' if split else 'no'))

            H = HivePlot(C.compose('GapJunction', 'Synapse', 'Monoamine'),
                             edge_colour_attribute="type", edge_category_legend=True,
                             edge_category_colours={'Synapse': 'Cyan', 'Monoamine': 'Magenta', 'GapJunction': 'Yellow'}, **def_args)
            H.draw(save_path='img/compare_layers_{}/{}_{}_{}_{}split.pdf'.format(order_by, source, 'whole', order_by, '' if split else 'no'))


print('done')