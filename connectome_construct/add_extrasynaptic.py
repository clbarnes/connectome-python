from construct_chklovskii import connectome as G

monoamine_path = '/home/cbarnes/data/connectome/monoamine_edgelist_labelled.txt'
neuropeptide_path = '/home/cbarnes/data/connectome/neuropeptide_edgelist_labelled.txt'


def add_monoamine(G):
    G = G.copy()
    transmitters = {'DOP': 'dopamine', 'SER': 'serotonin', 'TYR': 'tyramine', 'OCT': 'octopamine'}

    nodeset = set(G.nodes())

    with open(monoamine_path, 'r') as data_file:
        for row in data_file:
            src, tgt, weight, transmitter = row.strip().split()

            if {src, tgt}.issubset(nodeset):
                weight, transmitter = round(float(weight)), transmitters[transmitter]

                G.add_edge(src, tgt, attr_dict={'weight': weight, 'transmitter': transmitter, 'type': 'Monoamine'})

    return G


def add_neuropeptide(G):
    G = G.copy()
    nodeset = set(G.nodes())

    with open(neuropeptide_path, 'r') as data_file:

        for row in data_file:
            src, tgt, weight, transmitter = row.strip().split()

            if {src, tgt}.issubset(nodeset):
                weight = round(float(weight))

                G.add_edge(src, tgt, attr_dict={'weight': weight, 'transmitter': transmitter, 'type': 'Neuropeptide'})

    return G


def add_extrasynaptic(G):
    connectome = G.copy()
    connectome = add_monoamine(connectome)
    connectome = add_neuropeptide(connectome)

    return connectome