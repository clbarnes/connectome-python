from hiveplotter import HivePlot
import networkx as nx
from multiplex import MultiplexConnectome

order = ['ac', 'ww']

paths = ['/home/cbarnes/data/connectome/networks/{}_complete.gpickle'.format(key) for key in order]

graphs = [nx.read_gpickle(path) for path in paths]

connectomes = [MultiplexConnectome(graph) for graph in graphs]

for name, connectome in zip(order, connectomes):
    print('Doing {} network'.format(name))
    # whole network
    print('    whole')
    H_whole = HivePlot(connectome.whole, node_class_attribute="type", node_class_values=["interneuron", "motor", "sensory"],
             edge_colour_attribute="type", node_superimpose_representation="size",
             split_axes=["interneuron", "motor", "sensory"], edge_thickness_range=(0.003, 0.003),
             order_nodes_by='degree', edge_category_colours={
        "Synapse": "Cyan", "Monoamine": "Magenta", "GapJunction": "Yellow", 'Neuropeptide': 'White'
            }, edge_alpha=0.25, edge_category_legend=True, label_size=14)
    H_whole.draw(save_path='img/all_plots/{}_whole_deg.pdf'.format(name))

    # GJ
    print('    gapjunction')
    H = HivePlot(connectome['GapJunction'], parent_hiveplot=H_whole, node_class_attribute="type", node_class_values=["interneuron", "motor", "sensory"],
             edge_colour_attribute="weight", node_superimpose_representation="size",
             split_axes=["interneuron", "motor", "sensory"], edge_colour_gradient='RedWhite', edge_thickness_range=(0.003, 0.003),
             edge_alpha=0.25, label_size=14)
    H.draw(save_path='img/all_plots/{}_gj_deg.pdf'.format(name))

    # syn
    print('    synapse')
    H = HivePlot(connectome['Synapse'], parent_hiveplot=H_whole, node_class_attribute="type", node_class_values=["interneuron", "motor", "sensory"],
             edge_colour_attribute="weight", node_superimpose_representation="size",
             split_axes=["interneuron", "motor", "sensory"], edge_colour_gradient='RedWhite', edge_thickness_range=(0.003, 0.003),
             edge_alpha=0.25, label_size=14)
    H.draw(save_path='img/all_plots/{}_syn_deg.pdf'.format(name))

    # MA
    print('    ma')
    H = HivePlot(connectome['Monoamine'], parent_hiveplot=H_whole, node_class_attribute="type", node_class_values=["interneuron", "motor", "sensory"],
             edge_colour_attribute="transmitter", node_superimpose_representation="size",
             split_axes=["interneuron", "motor", "sensory"], edge_colour_gradient='Rainbow', edge_category_legend=True, edge_thickness_range=(0.003, 0.003),
             edge_alpha=0.25, label_size=14)
    H.draw(save_path='img/all_plots/{}_ma_deg.pdf'.format(name))

    #NP
    print('    np')
    H = HivePlot(connectome['Neuropeptide'], parent_hiveplot=H_whole, node_class_attribute="type", node_class_values=["interneuron", "motor", "sensory"],
             edge_colour_attribute="receptor", node_superimpose_representation="size",
             split_axes=["interneuron", "motor", "sensory"], edge_colour_gradient='Rainbow', edge_category_legend=True, edge_thickness_range=(0.003, 0.003),
             edge_alpha=0.25, label_size=14)
    H.draw(save_path='img/all_plots/{}_np_deg.pdf'.format(name))
#
# with open('img/all_plots/README.txt', 'w') as out_file:
#     out_file.write("""\
# HOW TO READ:
# All: nodes arrayed by degree *based on the whole graph* (i.e. persistent across subgraphs)
# whole: edges coloured by subgraph
# GJ: edges coloured red to white by weight
# syn: edges coloured red to white by weight
# MA: edges coloured by transmitter
# NP: edges coloured by receptor\
# """)