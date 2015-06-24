from util import data, plot_tools
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
from itertools import accumulate

PROPORTIONS = True

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()

types = ['Monoamine', 'Synapse', 'GapJunction']

colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

count_born_at_time = {tp: None for tp in types}
for tp in types:
    count_born_at_time[tp] = Counter(edge_birthtimes_by_type[tp])

all_birthtimes = {0, 3000}
for birthtimes in edge_birthtimes_by_type.values():
    all_birthtimes = all_birthtimes.union(birthtimes)

ordered_birthtimes = list(sorted(all_birthtimes))

full_counts = dict()

for tp in count_born_at_time:
    full_counts[tp] = list(accumulate([count_born_at_time[tp].get(birthtime, 0) for birthtime in ordered_birthtimes]))

arr = np.array([full_counts[tp] for tp in types] + [[0 for _ in range(len(full_counts[types[0]]))]], dtype=float)

arr[1, :] += arr[2, :]
arr[0, :] += arr[1, :]

if PROPORTIONS:
    div_by = np.copy(arr[0, :])
    div_by[div_by == 0] = 1
    for row_ind in range(np.shape(arr)[0]):
        arr[row_ind, :] = arr[row_ind, :] / div_by

fig = plt.figure()
ax = fig.add_subplot(111)

for ind, row in enumerate(arr[:3]):
    ax.fill_between(ordered_birthtimes, row, arr[ind+1], facecolor=colours[types[ind]])
    plt.plot([], [], color=colours[types[ind]], linewidth=10)

ax.legend(types, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
          ncol=3, mode="expand",
          borderaxespad=0)

ax.set_xlabel('Time (mins)')
if PROPORTIONS:
    ax.set_ylabel('Proportion of connections')
else:
    ax.set_ylabel('Connections born')

limits = list(ax.axis())
limits[0], limits[1] = ordered_birthtimes[np.where(arr[0,:] != 0)[0][0]], 3000
ax.axis(limits)
plot_tools.add_vlines_by_time(ax, ax.axis()[3]*0.95)

plt.show()

pass