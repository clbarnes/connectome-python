from matplotlib import pyplot as plt
from util import data
from scipy.stats import gaussian_kde
import numpy as np


LOG = False
CUMU = False


def get_kde_data(data):
    kde = gaussian_kde(data)
    ind = np.linspace(min(data), max(data), 100)
    y = kde(ind)
    y /= np.sum(y)
    return ind, y


def get_cumu_kde_data(data):
    x, y = get_kde_data(data)
    cumsum = np.cumsum(y)
    y = cumsum/np.max(cumsum)
    return x, y


colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()
edge_lengths_by_type = data.edge_lengths_by_type()

types = list(edge_birthtimes_by_type)

birthtime_data = [edge_birthtimes_by_type[key] for key in types]
length_data = [edge_lengths_by_type[key] for key in types]

ylabel = '{}Frequency'.format('Cumulative ' if CUMU else '')

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

for tp in types:
    x, y = get_cumu_kde_data(edge_birthtimes_by_type[tp]) if CUMU else get_kde_data(edge_birthtimes_by_type[tp])
    ax1.plot(x, y, color=colours[tp])

ax1.set_ylabel(ylabel)
ax1.set_xlabel('Edge birthtime (min)')
if LOG:
    ax1.set_xscale('log')
ax1.legend(types, loc=4 if CUMU else 1)

for tp in types:
    x, y = get_cumu_kde_data(edge_lengths_by_type[tp]) if CUMU else get_kde_data(edge_lengths_by_type[tp])
    ax2.plot(x, y, color=colours[tp])

ax2.set_ylabel(ylabel)
ax2.set_xlabel('Edge length (mm)')
if LOG:
    ax2.set_xscale('log')
ax2.legend(types, loc=4 if CUMU else 1)

fig.suptitle('Comparison of edge lengths and birth times')

plt.show()
