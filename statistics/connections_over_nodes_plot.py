from util import data, plot_tools
from matplotlib import pyplot as plt
from collections import Counter
from itertools import accumulate
from scipy.interpolate import interp1d

NORMALISED = False
"""Whether to scale y axis for each line to allow comparison of growth rates at different time points"""
interp_kind = 'zero'

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()

types = list(edge_birthtimes_by_type)

colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

node_count_times, node_counts = data.get_node_counts_at_times()

fig = plt.figure()
ax = fig.add_subplot(111)

for tp in types:
    edges_born_at_times = Counter(edge_birthtimes_by_type[tp])

    x_data = [0] + list(sorted(edges_born_at_times)) + [3000]
    y_data = list(accumulate([edges_born_at_times.get(i, 0) for i in x_data]))

    get_y = interp1d(x_data, y_data, kind=interp_kind)

    if NORMALISED:
        y = [get_y(t) / len(edge_birthtimes_by_type[tp]) for t in node_count_times]
    else:
        y = [get_y(t) for t in node_count_times]

    ax.plot(node_counts, y, c=colours[tp])

ax.set_xlabel('Nodes born')
if NORMALISED:
    ax.set_ylabel('Proportion of final connections')
else:
    ax.set_ylabel('Number of connections')
ax.set_title('Number of connections over nodes born')
if NORMALISED:
    ax.axis([0, max(node_counts), 0, 1])
else:
    extents = list(ax.axis())
    extents[1] = max(node_counts)
    ax.axis(extents)
ax.legend(types, loc=4)
scaling_factor = 0.5 if NORMALISED else 0.95
plot_tools.add_vlines_by_nodes_born(ax, ax.axis()[3]*scaling_factor)

plt.show()