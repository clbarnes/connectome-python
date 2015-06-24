from util import data, plot_tools
from matplotlib import pyplot as plt
from collections import Counter
from itertools import accumulate

NORMALISED = False
"""Whether to scale y axis for each line to allow comparison of growth rates at different time points"""

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()

types = list(edge_birthtimes_by_type)

colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

fig = plt.figure()
ax = fig.add_subplot(111)

for tp in types:
    edges_born_at_times = Counter(edge_birthtimes_by_type[tp])

    x = list(sorted(edges_born_at_times))
    plot_tools.pad_time_list(x)

    if NORMALISED:
        y = list(accumulate([edges_born_at_times[i] / len(edge_birthtimes_by_type[tp]) for i in x]))
    else:
        y = list(accumulate([edges_born_at_times[i] for i in x]))

    plot_tools.pad_y_list(y)
    ax.plot(plot_tools.pad_time_list(x), plot_tools.pad_y_list(y), c=colours[tp])

ax.set_xlabel('Time (min)')
if NORMALISED:
    ax.set_ylabel('Proportion of final connections')
else:
    ax.set_ylabel('Number of connections')
ax.set_title('Number of connections over time')
ax.legend(types, loc=4)
scaling_factor = 0.5 if NORMALISED else 0.95
plot_tools.add_vlines_by_time(ax, ax.axis()[3]*scaling_factor)

plt.show()

pass