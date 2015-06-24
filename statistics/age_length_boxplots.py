from matplotlib import pyplot as plt
from util import data

C, M = data.get_length_and_birthtime()

edge_birthtimes_by_type = data.edge_birthtimes_by_type()
edge_lengths_by_type = data.edge_lengths_by_type()

types = list(edge_birthtimes_by_type)

colours = {
    'GapJunction': 'y',
    'Synapse': 'c',
    'Monoamine': 'm'
}

birthtime_data = [edge_birthtimes_by_type[key] for key in types]
length_data = [edge_lengths_by_type[key] for key in types]

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.boxplot(birthtime_data)#, labels=types)
ax1.set_ylabel('Edge birth time (minutes)')
ax1.set_xlabel('Edge type ({})'.format(', '.join(types)))

ax2.boxplot(length_data)#, labels=types)
ax2.set_ylabel('Edge length (mm)')
ax2.set_xlabel('Edge type ({})'.format(', '.join(types)))

fig.suptitle('Comparison of edge lengths and birth times')

plt.show()
