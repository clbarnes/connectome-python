from multiplex import MultiplexConnectome
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

path = '/home/cbarnes/data/connectome/networks/ww_complete.gpickle'

ww = MultiplexConnectome(nx.read_gpickle(path))

ma_lengths = np.array(list(nx.get_edge_attributes(ww['Monoamine'], 'min_length').values()))
np_lengths = np.array(list(nx.get_edge_attributes(ww['Neuropeptide'], 'min_length').values()))

bins = np.linspace(0, 655, 50)

plt.hist(ma_lengths, bins=bins, normed=True, alpha=0.5, label='Monoamine', color='b')
plt.hist(np_lengths, bins=bins, normed=True, alpha=0.5, label='Neuropeptide', color='r')
plt.legend()
# plt.yscale('log')
plt.show()