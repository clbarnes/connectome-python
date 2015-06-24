import networkx as nx
import os
import re
from node_data import add_all

root_path = '/home/cbarnes/data/connectome/networks/EdgeLists'


def add_edges_from_file(graph, path, **kwargs):
    with open(path, 'r') as data_file:
        for row in (row.strip() for row in data_file):
            src, tgt, weight = row.split(' ')
            graph.add_edge(src, tgt, weight=float(weight), attr_dict=kwargs.copy())


def get_synaptic(graph, which):
    """
    :param which: 'WW' or 'AC'
    :return:
    """

    G = graph.copy()
    syn_path = os.path.join(root_path, 'edgeL_{}_syn.txt'.format(which))
    add_edges_from_file(G, syn_path, type='Synapse', source=which)
    return G


def get_gapjunction(graph, which):
    """

    :param graph:
    :param which: 'WW' or 'AC'
    :return:
    """

    G = graph.copy()
    gap_path = os.path.join(root_path, 'edgeL_{}_gap.txt'.format(which))
    add_edges_from_file(G, gap_path, type='GapJunction', source=which)
    return G


def get_monoamine(graph, full=True):
    """

    :param graph:
    :return:
    """

    G = graph.copy()

    if not full:
        ma_path = os.path.join(root_path, 'edgeL_monoamine.txt'.format())
        add_edges_from_file(G, ma_path, type='Monoamine')
        return G

    rec_to_mol = {'DOP-1': 'dopamine',
                  'DOP-2': 'dopamine',
                  'DOP-3': 'dopamine',
                  'DOP-4': 'dopamine',
                  'DOP-5': 'dopamine',
                  'DOP-6': 'dopamine',
                  'LGC-55': 'tyramine',
                  'MOD-1': 'serotonin',
                  'OCTR-1': 'octopamine',
                  'SER-1': 'serotonin',
                  'SER-2': 'serotonin',
                  'SER-3': 'serotonin',
                  'SER-4': 'serotonin',
                  'SER-5': 'serotonin',
                  'SER-6': 'serotonin',
                  'SER-7': 'serotonin',
                  'TYRA-2': 'tyramine',
                  'TYRA-3': 'tyramine'}

    data_path = os.path.join(root_path, 'Monoamine', 'Receptors')

    for file_path in os.listdir(data_path):
        receptor = re.search('edgeL_(.*)\.txt', file_path).group(1)
        add_edges_from_file(G, os.path.join(data_path, 'edgeL_{}.txt'.format(receptor)), type='Monoamine',
                            transmitter=rec_to_mol[receptor], receptor=receptor)

    return G


def get_neuropeptide(graph, full=True):
    """

    :param graph:
    :return:
    """

    G = graph.copy()

    if not full:
        ma_path = os.path.join(root_path, 'edgeL_neuropeptide.txt'.format())
        add_edges_from_file(G, ma_path, type='Neuropeptide')
        return G

    data_path = os.path.join(root_path, 'Neuropeptide')

    for file_path in os.listdir(data_path):
        receptor = re.search('edgeL_(.*)\.txt', file_path).group(1)
        add_edges_from_file(G, os.path.join(data_path, 'edgeL_{}.txt'.format(receptor)), type='Neuropeptide',
                            receptor=receptor)

    return G

WW_G = nx.MultiDiGraph()
WW_G = get_synaptic(WW_G, 'WW')
WW_G = get_gapjunction(WW_G, 'WW')
WW_G = get_monoamine(WW_G)
WW_G = get_neuropeptide(WW_G)
WW_G = add_all(WW_G)
nx.write_gpickle(WW_G, '/home/cbarnes/data/connectome/networks/ww_complete.gpickle')


AC_G = nx.MultiDiGraph()
AC_G = get_synaptic(AC_G, 'AC')
AC_G = get_gapjunction(AC_G, 'AC')
AC_G = get_monoamine(AC_G)
AC_G = get_neuropeptide(AC_G)
AC_G = add_all(AC_G)
nx.write_gpickle(AC_G, '/home/cbarnes/data/connectome/networks/ac_complete.gpickle')