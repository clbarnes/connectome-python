import connectome_utils as utl
import networkx as nx
from multiplex import MultiplexConnectome
from multiprocessing import Pool, cpu_count
from scipy import io as sio
import numpy as np


order = ['ac', 'ww']

paths = ['/home/cbarnes/data/connectome/networks/{}_complete.gpickle'.format(key) for key in order]

graphs = [nx.read_gpickle(path) for path in paths]

connectomes = [MultiplexConnectome(graph) for graph in graphs]


def mean(iterable):
    return sum(iterable)/len(iterable)


def single_random_path_length(graph):
    return av_path_length(utl.randomise_network(graph))


def control_path_length(graph, n=50):
    G = nx.create_empty_copy(graph, with_nodes=True)
    G.add_edges_from(graph.edges_iter())
    with Pool(cpu_count()) as p:
        return p.map(single_random_path_length, (G.copy() for _ in range(n)))


def av_path_length(graph):
    return key_key_av(nx.shortest_path_length(graph))


def key_key_av(dict_of_dicts):
    d = dict_of_dicts
    vals = [val for inner in d.values() for val in inner.values()]
    return mean(vals)


def sensorimotor_pathlength(G):
    sensory = set()
    motor = set()

    for node, data in G.nodes_iter(data=True):
        if 'sensor' in data.get('description_wa', None).lower():
            sensory.add(node)
        if 'motor' in data.get('description_wa', None).lower():
            motor.add(node)

    lengths = {src: {tgt: nx.shortest_path_length(G, source=src, target=tgt)} for src in sensory for tgt in motor}

    return key_key_av(lengths)


def clean_graph(G):
    out_graph = nx.DiGraph()
    out_graph.add_nodes_from(G.nodes_iter())
    out_graph.add_edges_from(G.edges_iter())
    return out_graph


def to_binarised_adj(G):
    graph = clean_graph(G)
    return nx.to_numpy_matrix(graph, sorted(graph.nodes_iter()))


def iterate_adj_mats(path):
    data = sio.loadmat(path)
    node_mapping = {i: node for i, node in enumerate(data['nodelist'])}
    for key, value in data.items():
        if type(value) == np.array and np.shape(value) == (302, 302) and not key.endswith('source'):
            G = nx.from_numpy_matrix(data[key])
            nx.relabel_nodes(G, node_mapping)
            yield G


