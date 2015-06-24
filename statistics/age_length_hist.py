from matplotlib import pyplot as plt
from util import data
from scipy.stats import gaussian_kde
import numpy as np
from math import log


LOG = False
BINS = 20
NORM = False

def log_all_if_log(data):
    """

    :type data: list of lists
    """
    if LOG:
        return [[log(n) if n else 0 for n in lst] for lst in data]
    else:
        return data

# def get_weights_if_norm(data):
#
#     :param data:
#     :type data: list of list
#     :return:
#     :rtype:
#     """
#     if NORM:
#         sums = [sum(lst) for lst in data]
#         weights = [s/max(sums) for s in sums]
#         return [[weights[i] for _ in data[i]] for i in range(len(data))]
#     else:
#         return [[1 for _ in lst] for lst in data]

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

ylabel = '{}Frequency'.format('Relative ' if NORM else '')

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.hist(log_all_if_log(birthtime_data), bins=BINS, color=[colours[tp] for tp in types])

ax1.set_ylabel(ylabel)
ax1.set_xlabel('Edge birthtime (min)')
ax1.legend(types, loc=1)

ax2.hist(log_all_if_log(length_data), bins=BINS, color=[colours[tp] for tp in types])

ax2.set_ylabel(ylabel)
ax2.set_xlabel('Edge length (mm)')
ax2.legend(types, loc=1)

fig.suptitle('Comparison of edge lengths and birth times')

plt.show()