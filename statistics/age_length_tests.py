from matplotlib import pyplot as plt
from util import data
import scipy.stats
import numpy as np

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()
edge_lengths_by_type = data.edge_lengths_by_type()

types = list(sorted(edge_birthtimes_by_type))

colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

birthtime_data = [edge_birthtimes_by_type[key] for key in types]
length_data = [edge_lengths_by_type[key] for key in types]

birthtime_output = np.empty([3,3], dtype=float)
length_output = np.copy(birthtime_output)

for ind1, tp1 in enumerate(types):
    for ind2, tp2 in enumerate(types):
        _, birthtime_output[ind1, ind2] = scipy.stats.mannwhitneyu(birthtime_data[ind1], birthtime_data[ind2])
        _, length_output[ind1, ind2] = scipy.stats.mannwhitneyu(length_data[ind1], length_data[ind2])

fig, axes = plt.subplots(nrows=2, ncols=2)
bt_colour_ax, len_colour_ax, bt_bool_ax, len_bool_ax = axes.flat

im = bt_colour_ax.imshow(birthtime_output, vmin=0, vmax=1, interpolation='nearest')
im = len_colour_ax.imshow(length_output, vmin=0, vmax=1, interpolation='nearest')
im = bt_bool_ax.imshow(birthtime_output < 0.05, vmin=0, vmax=1, interpolation = 'nearest')
im = len_bool_ax.imshow(length_output < 0.05, vmin=0, vmax=1, interpolation = 'nearest')

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

bt_colour_ax.set_title('Edge birth time distribution')
len_colour_ax.set_title('Edge length distribution')
bt_colour_ax.set_ylabel('p-value from 1-sided MWU test')
bt_bool_ax.set_ylabel('Significance at p = 0.05')

for ax in axes.flat:
    for this_ax in [ax.xaxis, ax.yaxis]:
        this_ax.set_ticks([0, 1, 2])
        this_ax.set_ticklabels(types)

plt.show()