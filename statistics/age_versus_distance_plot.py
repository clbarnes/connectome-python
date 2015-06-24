from matplotlib import pyplot as plt
from util import data

C, M = data.get()

edge_by_type = dict()
for start, stop, data in C.edges_iter(data=True):
    if any(['birthtime' not in C.node[start], 'birthtime' not in C.node[stop],
            'length' not in data]):
        continue

    if data['type'] not in edge_by_type:
        edge_by_type[data['type']] = {'birthtime': [], 'length': []}

    edge_by_type[data['type']]['birthtime'].append(max([C.node[start]['birthtime'], C.node[stop]['birthtime']]))
    edge_by_type[data['type']]['length'].append(data['length'])

colour_and_shape = {
    'GapJunction': {'c': 'y', 'marker': 'o'},
    'Synapse': {'c': 'c', 'marker': 's'},
    'Monoamine': {'c': 'm', 'marker': 'd'}
}

edge_types = list(edge_by_type)

fig = plt.figure()
ax = fig.add_subplot(111)
for edge_type in edge_types:
    ax.scatter(edge_by_type[edge_type]['birthtime'], edge_by_type[edge_type]['length'], **colour_and_shape[edge_type])

ax.legend(edge_types)
ax.set_xlabel('Birth time (minutes)')
ax.set_ylabel('Length (mm)')
ax.set_title('Distance between cell bodies of neighbouring nodes vs birth time of youngest node')

plt.show()