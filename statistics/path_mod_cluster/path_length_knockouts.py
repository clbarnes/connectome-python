from shared import order, connectomes, control_path_length, av_path_length
import connectome_utils as utl
import networkx as nx
import json
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
from multiplex import MultiplexConnectome
from scipy import stats
from stats_utils import zscore


raw_lengths_path = 'path_length_output.json'
output_path = 'path_length_knockout_phys_output.json'

d = dict(zip(order, connectomes))

physical_n = ['GapJunction', 'Synapse']
extrasyn_n = ['Monoamine', 'Neuropeptide']

with open(raw_lengths_path, 'r') as data_file:
    out = json.load(data_file)

to_knock_out = {'transmitters': set(), 'receptors': set()}

for _1, _2, data in d['ww'].whole.edges_iter(data=True):
    to_knock_out['transmitters'].add(data.get('transmitter', None))
    to_knock_out['receptors'].add(data.get('receptor', None))

for st in to_knock_out.values():
    st.remove(None)


knocked_out = dict()

for network_id in order:
    print('Processing {}'.format(network_id))
    knocked_out[network_id] = {'transmitter': dict(), 'receptor': dict()}

    G = d[network_id].whole

    for transmitter in to_knock_out['transmitters']:
        knocked_out[network_id]['transmitter'][transmitter] = dict()
        print('    Processing transmitter {}'.format(transmitter))
        temp_graph = MultiplexConnectome(utl.knockout(G, transmitter=transmitter)).collapse()
        actual_length = av_path_length(temp_graph)
        control_path_lengths = control_path_length(temp_graph, 100)
        actual_length_z = zscore(actual_length, control_path_lengths)
        control_path_lengths_z = list(stats.zscore(control_path_lengths))
        knocked_out[network_id]['transmitter'][transmitter]['actual_length'] = actual_length
        knocked_out[network_id]['transmitter'][transmitter]['actual_length_z'] = actual_length_z
        knocked_out[network_id]['transmitter'][transmitter]['control_lengths'] = control_path_lengths
        knocked_out[network_id]['transmitter'][transmitter]['control_lengths_z'] = control_path_lengths_z
        with open(output_path, 'w') as out_file:
            json.dump(knocked_out, out_file)

    for receptor in to_knock_out['receptors']:
        knocked_out[network_id]['receptor'][receptor] = dict()
        print('    Processing receptor {}'.format(receptor))
        temp_graph = MultiplexConnectome(utl.knockout(G, receptor=receptor)).collapse()
        actual_length = av_path_length(temp_graph)
        control_path_lengths = control_path_length(temp_graph, 100)
        actual_length_z = zscore(actual_length, control_path_lengths)
        control_path_lengths_z = list(stats.zscore(control_path_lengths))
        knocked_out[network_id]['receptor'][receptor]['actual_length'] = actual_length
        knocked_out[network_id]['receptor'][receptor]['actual_length_z'] = actual_length_z
        knocked_out[network_id]['receptor'][receptor]['control_lengths'] = control_path_lengths
        knocked_out[network_id]['receptor'][receptor]['control_lengths_z'] = control_path_lengths_z
        with open(output_path, 'w') as out_file:
            json.dump(knocked_out, out_file)