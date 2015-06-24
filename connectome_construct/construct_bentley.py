from networkx import nx

gj_path = '/home/cbarnes/data/connectome/networks/EdgeLists/edgeL_gap.txt'
syn_path = '/home/cbarnes/data/connectome/networks/EdgeLists/edgeL_syn.txt'
ma_path = '/home/cbarnes/data/connectome/networks/EdgeLists/edgeL_monoamine.txt'
np_path = '/home/cbarnes/data/connectome/networks/EdgeLists/edgeL_neuropeptide.txt'
node_birthtime_path = '/home/cbarnes/data/connectome/birthtime_location.csv'
wormatlas_path = '/home/cbarnes/data/connectome/worm_atlas_neuron_data.tsv'


def add_edges_from(G, path, ctype=''):
    with open(path, 'r') as data_file:
        for row in data_file:
            src, tgt, weight = row.split(' ')
            weight = float(weight)

            G.add_edge(src, tgt, weight=weight, type=ctype)


def add_wormatlas_data(G, path):
    node_data = dict()
    with open(path, 'r') as data_file:
        for row in data_file:
            node, lineage, description = row.strip().split('\t')
            node_data[node] = {'lineage': lineage, 'description': description}

    for node, data in G.nodes_iter(data=True):
        if node not in node_data:
            data.update({'lineage': '', 'description': '', 'type': ''})
            continue

        data.update(node_data[node])

        if 'interneuron' in data['description']:
            data['type'] = 'interneuron'
        elif 'motor' in data['description']:
            data['type'] = 'motor'
        elif 'sensory' in data['description']:
            data['type'] = 'sensory'
        else:
            data['type'] = 'interneurone'

def add_length_birthtime(G, path):
    node_data = dict()
    with open(path, 'r') as data_file:
        next(data_file)
        for row in data_file:
            cell, birthtime, x, y = row.strip().split(',')
            node_data[cell] = {'birthtime': birthtime, 'position': (float(x), float(y))}

    for node, data in G.nodes_iter(data=True):
        data.update(node_data.get(node, {'birthtime': None, 'position': None}))

    return G

G = nx.MultiDiGraph()

add_edges_from(G, gj_path, ctype='GapJunction')
add_edges_from(G, syn_path, ctype='Synapse')
add_edges_from(G, ma_path, ctype='Monoamine')
add_edges_from(G, np_path, ctype='Neuropeptide')

add_wormatlas_data(G, wormatlas_path)
add_length_birthtime(G, node_birthtime_path)

nx.write_gpickle(G, '/home/cbarnes/data/connectome/networks/gj-ma-np-syn_ben_herm.gpickle')