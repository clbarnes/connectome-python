print('Setting up')

import json

from scipy import stats
from stats_utils import zscore

from path_mod_cluster.shared import order, connectomes, control_path_length, av_path_length

from_scratch = False

# plt.style.use('ggplot')

print('Getting data')
out_path = 'path_length_output.json'

d = dict(zip(order, connectomes))

physical_n = ['GapJunction', 'Synapse']
extrasyn_n = ['Monoamine', 'Neuropeptide']


if from_scratch:
    out = dict()
    for network in d:
        physical = d[network].collapse(*physical_n)
        whole = d[network].collapse()

        print('Network: {}'.format(network))
        print(' Getting physical raw length')
        physical_length = av_path_length(physical)
        print(' Getting physical control lengths')
        physical_control_lengths = control_path_length(physical, 100)
        print(' Getting whole raw length')
        whole_length = av_path_length(whole)
        print(' Getting whole control lengths')
        whole_control_lengths = control_path_length(whole, 100)

        out[network] = {
            'physical': {
                'actual_length': physical_length,
                'actual_length_z': zscore(physical_length, physical_control_lengths),
                'control_lengths': physical_control_lengths,
                'control_lengths_z': stats.zscore(physical_control_lengths)
            },
            'whole': {
                'actual_length': whole_length,
                'actual_length_z': zscore(whole_length, whole_control_lengths),
                'control_lengths': whole_control_lengths,
                'control_lengths_z': stats.zscore(whole_control_lengths)
            }
        }

    try:
        with open(out_path, 'w') as out_file:
            json.dump(out, out_file)
    except:
        print('There was a problem! Write output manually.')
else:
    with open(out_path, 'r') as out_file:
        out = json.load(out_file)

print('Got data')

actual_zscores = []
control_zscores = []

for network in ['ac', 'ww']:
    for completeness in ['physical', 'whole']:

        actual_zscores.append(zscore(
            out[network][completeness]['actual_length'], out[network][completeness]['control_lengths']
        ))

        control_zscores.append(stats.zscore(out[network][completeness]['control_lengths']))

pvals = stats.norm.sf(actual_zscores)

print('Done')

