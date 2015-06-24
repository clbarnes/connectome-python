import networkx as nx
from multiplex import MultiplexConnectome
import community
import numpy as np
from matplotlib import pyplot as plt

sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

di_phys = {source: C[source].compose('Synapse', 'GapJunction') for source in sources}
undi_phys = {source: nx.Graph(di_phys[source]) for source in sources}


def get_cliqueset(G):
    return {frozenset(nodelist) for nodelist in nx.find_cliques(G)}

ww_cliques = get_cliqueset(undi_phys['ww'])
ac_cliques = get_cliqueset(undi_phys['ac'])

len(ac_cliques & ww_cliques)