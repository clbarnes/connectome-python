import networkx as nx

connectivity_path = '/home/cbarnes/data/connectome/chklovskii/NeuronConnect.csv'
type_path = '/home/cbarnes/data/connectome/chklovskii/NeuronType.csv'


def add_nodes(G):
    # do nodes
    G = G.copy()

    floats = {'Soma Position'}
    ints = {'TotHead', 'TotTail', 'TotMid', 'S_Head', 'R_Head', 'S_Mid', 'R_Mid', 'S_Tail', 'R_Tail', 'AYNbr'}

    names = {'Soma Position': 'AP_position',
             'Soma Region': 'region',
             'Span': 'span',
             'Ambiguity': 'ambiguity',
             'TotHead': 'total_head',
             'TotTail': 'total_tail',
             'TotMid': 'total_mid',
             'S_Head': 'send_head',
             'R_Head': 'receive_head',
             'S_Mid': 'send_mid',
             'R_Mid': 'receive_mid',
             'S_Tail': 'send_tail',
             'R_Tail': 'receive_tail',
             'AY Ganglion Designation': 'ganglion',
             'AYNbr': 'id'}

    regions = {'H': 'head', 'M': 'mid', 'T': 'tail'}
    spans = {'S': 'short', 'L': 'long'}

    with open(type_path, 'r') as data_file:
        labels = next(data_file).strip().split(',')

        for row in data_file:
            row_data = dict(zip((label.strip() for label in labels), (item.strip() for item in row.strip().split(','))))

            for key in floats:
                row_data[key] = float(row_data[key])
            for key in ints:
                row_data[key] = int(row_data[key])

            attr_dict = {new_name: row_data[old_name] for old_name, new_name in names.items()}
            attr_dict['region'] = regions[attr_dict['region']]
            attr_dict['span'] = spans[attr_dict['span']]

            G.add_node(row_data['Neuron'], attr_dict=attr_dict)
    return G


def get_nodelist(G):
    if len(G.nodes()) == 0:
        G = add_nodes(nx.MultiDiGraph())

    IDs = nx.get_node_attributes(G, 'id')

    return [pair[0] for pair in sorted(IDs.items(), key=lambda x: x[1])]


def add_edges(G):
    # do edges
    G = G.copy()
    names = {'Type': 'type'}

    ints = {'Nbr'}

    types = {'EJ': 'GapJunction', 'S': 'Synapse', 'Sp': 'Synapse'}

    with open(connectivity_path, 'r') as data_file:
        labels = next(data_file).strip().split(',')

        for row in data_file:
            row_data = dict(zip((label.strip() for label in labels), (item.strip() for item in row.strip().split(','))))
            if row_data['Type'] not in types:
                continue

            src, tgt = row_data['Neuron 1'], row_data['Neuron 2']

            for key in ints:
                row_data[key] = int(row_data[key])
            attr_dict = {new_name: row_data[old_name] for old_name, new_name in names.items()}
            attr_dict['type'] = types[attr_dict['type']]
            attr_dict['weight'] = 1

            for _ in range(row_data['Nbr']):
                G.add_edge(src, tgt, attr_dict=attr_dict)
    return G


def construct():
    connectome = nx.MultiDiGraph()
    connectome = add_nodes(connectome)
    connectome = add_edges(connectome)
    return connectome


connectome = construct()