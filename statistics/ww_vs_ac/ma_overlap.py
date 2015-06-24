from multiplex import MultiplexConnectome
import connectome_utils as utl
import networkx as nx
from scipy import io as sio
import os
import numpy as np
import json
import scipy.stats as st


def ppn_ma_edges_w_parallel_syn(ma, syn):
    """
    The proportion of monoamine edges which have a parallel synapse
    """
    syn_edgeset = set(syn.edges_iter())
    return np.mean([edge in syn_edgeset for edge in ma.edges_iter()])


def ppn_syn_from_ma_nodes_w_parallel_ma(ma, syn):
    """
    The proportion of synapses, whose source node expresses a monoamine, which have a parallel MA edge
    """
    ma_edgeset = set(ma.edges_iter())
    ma_sources = {src for src, tgt in ma_edgeset}

    return np.mean([edge in ma_edgeset for edge in syn.edges_iter() if edge[0] in ma_sources])


def min_ppn_only_extrasyn(ma, syn):
    """
    Each monoamine link is from an MA-expressing node to an receptor-expressing node. Receptors are specific to one MA; MAs are specific to one or more receptors.

    The proportion of receptor-expressing nodes which receive no synapses from nodes expressing the corresponding monoamine.
    """

    syn_edgeset = {edge for edge in syn.edges_iter()}

    receptor_to_MA = dict()
    receptor_to_nodes = dict()
    MA_to_nodes = dict()
    for src, tgt, data in ma.edges_iter(data=True):
        receptor = data['receptor']
        MA = data['transmitter']

        if receptor not in receptor_to_MA:
            receptor_to_MA[receptor] = MA
        if receptor not in receptor_to_nodes:
            receptor_to_nodes[receptor] = set()
        if MA not in MA_to_nodes:
            MA_to_nodes[MA] = set()

        receptor_to_nodes[receptor].add(tgt)
        MA_to_nodes[MA].add(src)

    # ret = []
    ret = {MA: [] for MA in MA_to_nodes}
    for receptor, tgts in receptor_to_nodes.items():
        srcs = MA_to_nodes[receptor_to_MA[receptor]]
        for tgt in tgts:
            ma_edges = {(src, tgt) for src in srcs}
            # ret.append(len(ma_edges & syn_edgeset) == 0)
            ret[receptor_to_MA[receptor]].append(len(ma_edges & syn_edgeset) == 0)

    # return np.mean(ret)
    return {key: np.mean(value) for key, value in ret.items()}

def iterate_adj_mats(path):
    data = sio.loadmat(path)
    var_name_stub = '{}_{}_'.format('ww' if '/ww/' in path else 'ac', path[path.rfind('/')+1:-4])
    node_mapping = {i: node for i, node in enumerate(data['nodelist'])}
    for var_name in (var_name_stub + str(i) for i in range(1000)):
        G = nx.from_numpy_matrix(data[var_name])
        yield nx.relabel_nodes(G, node_mapping)


def zval(val, mean, sd):
    return (val - mean) / sd


def z_to_p(z):
    return st.norm.cdf(z)


def pval(val, mean, sd):
    return st.norm.cdf(val, loc=mean, scale=sd)


sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

data_root = '/home/cbarnes/data/connectomes'

output_path = 'ma_overlap_data.json'

def generate_data():

    ppn1 = dict()
    ppn2 = dict()
    ppn3 = dict()

    for source in sources:
        print(source)

        ppn1[source] = dict()
        ppn2[source] = dict()
        ppn3[source] = dict()

        print('    ppn1')
        # proportion of monoamine edges which have a parallel synapse
        ppn1[source]['actual'] = ppn_ma_edges_w_parallel_syn(C[source]['Monoamine'], C[source]['Synapse'])

        ma_syn_iter = zip(
            iterate_adj_mats(os.path.join(data_root, 'randoms', source, 'layers', 'Monoamine.mat')),
            iterate_adj_mats(os.path.join(data_root, 'randoms', source, 'layers', 'Synapse.mat'))
        )

        ppn1[source]['control_full'] = [ppn_ma_edges_w_parallel_syn(ma, syn) for ma, syn in ma_syn_iter]
        ppn1[source]['control_mean'] = np.mean(ppn1[source]['control_full'])
        ppn1[source]['control_sd'] = np.std(ppn1[source]['control_full'])

        print('    ppn2')
        # proportion of synaptic edges, from a node with outward monoamine edges, which have parallel monoamine edges

        ppn2[source]['actual'] = ppn_syn_from_ma_nodes_w_parallel_ma(C[source]['Monoamine'], C[source]['Synapse'])

        ma_syn_iter = zip(
            iterate_adj_mats(os.path.join(data_root, 'randoms', source, 'layers', 'Monoamine.mat')),
            iterate_adj_mats(os.path.join(data_root, 'randoms', source, 'layers', 'Synapse.mat'))
        )

        ppn2[source]['control_full'] = [ppn_syn_from_ma_nodes_w_parallel_ma(ma, syn) for ma, syn in ma_syn_iter]
        ppn2[source]['control_mean'] = np.mean(ppn2[source]['control_full'])
        ppn2[source]['control_sd'] = np.std(ppn2[source]['control_full'])

        print('    ppn3')
        ppn3[source]['actual'] = min_ppn_only_extrasyn(C[source]['Monoamine'], C[source]['Synapse'])

        ppn3[source]['control_full'] = [ppn_syn_from_ma_nodes_w_parallel_ma(C[source]['Monoamine'], syn)
                                        for syn in iterate_adj_mats(os.path.join(data_root, 'randoms', source, 'layers', 'Synapse.mat'))]
        ppn3[source]['control_mean'] = np.mean(ppn3[source]['control_full'])
        ppn3[source]['control_sd'] = np.std(ppn3[source]['control_full'])

    ppn1['description'] = 'proportion of monoamine edges which have a parallel synapse'
    ppn2['description'] = 'proportion of synaptic edges, from a node with outward monoamine edges, \
    which have parallel monoamine edges'
    ppn3['description'] = 'The proportion of receptor-expressing nodes which receive at least one synapse from a node expressing the corresponding monoamine.'

    out_data = {
        'ppn1': ppn1,
        'ppn2': ppn2,
        'ppn3': ppn3
    }

    json.dump(out_data, open(output_path, 'w'), indent=4, sort_keys=True)


def analyse_data():
    pvals = dict()
    for ppn_name, ppn_d in data.items():
        pvals[ppn_name] = {'description': ppn_d['description']}
        for source_name, source_d in [(source, ppn_d[source]) for source in sources]:
            pvals[ppn_name][source_name] = pval(source_d['actual'], source_d['control_mean'], source_d['control_sd'])
    json.dump(pvals, open('ma_overlap_results.json', 'w'), indent=2, sort_keys=True)


# generate_data()
# data = json.load(open(output_path))
# analyse_data()

ppn3 = {source: min_ppn_only_extrasyn(C[source]['Monoamine'], C[source]['Synapse']) for source in sources}

print('done')