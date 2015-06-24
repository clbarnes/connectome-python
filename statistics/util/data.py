import networkx as nx
import os
import multiplex
from collections import Counter
from itertools import accumulate
from collections import OrderedDict
from scipy.interpolate import interp1d

home = '/home/cbarnes/'
C = nx.read_gpickle(os.path.join(home, 'data/connectome/full_connectome.gpickle'))

order_by_time = OrderedDict([
    ('Fertilisation', 0),
    ('Egg Laid', 150),
    ('Twitching', 470),
    ('Hatching (L1)', 840),
    ('L2', 1560),
    ('L3', 1980),
    ('L4', 2400),
    ('Adult', 2940)
])

def get():
    M = multiplex.MultiplexConnectome(C.copy())
    return C, M


def get_length_and_birthtime():
    C2 = C.copy()

    to_remove = []
    for node, data in C2.nodes_iter(data=True):
        if any(['position' not in data, 'birthtime' not in data]):
            to_remove.append(node)

    C2.remove_nodes_from(to_remove)

    for start, stop, data in C2.edges_iter(data=True):
        data['birthtime'] = max([C2.node[start]['birthtime'], C2.node[stop]['birthtime']])

    return C2, multiplex.MultiplexConnectome(C2)


def edge_birthtimes_by_type():
    C, _ = get_length_and_birthtime()
    birthtimes_by_type = dict()
    for start, stop, data in C.edges_iter(data=True):
        if data['type'] not in birthtimes_by_type:
            birthtimes_by_type[data['type']] = []

        birthtimes_by_type[data['type']].append(data['birthtime'])

    return birthtimes_by_type


def edge_lengths_by_type():
    C, _ = get_length_and_birthtime()
    lengths_by_type = dict()
    for start, stop, data in C.edges_iter(data=True):
        if data['type'] not in lengths_by_type:
            lengths_by_type[data['type']] = []

        lengths_by_type[data['type']].append(data['length'])

    return lengths_by_type


def get_node_counts_at_times(pad=True):
    C, _ = get_length_and_birthtime()
    node_birthtimes = nx.get_node_attributes(C, 'birthtime').values()

    node_birthtimes_counter = Counter(node_birthtimes)

    if pad:
        t = [0] + list(sorted(node_birthtimes_counter)) + [3000]
        n = list(accumulate([node_birthtimes_counter.get(time_point, 0) for time_point in t]))
    else:
        t = list(sorted(node_birthtimes_counter))
        n = list(accumulate([node_birthtimes_counter[time_point] for time_point in t]))

    return t, n


def get_order_by_nodes_born():
    node_count_times, node_counts = get_node_counts_at_times()
    get_count = interp1d(node_count_times, node_counts, kind='zero')
    return OrderedDict([(key, get_count(value)) for key, value in order_by_time.items()])

order_by_nodes_born = get_order_by_nodes_born()
