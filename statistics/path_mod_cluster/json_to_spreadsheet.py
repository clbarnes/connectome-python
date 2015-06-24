import json

path = 'tmp.csv'
y_order = ['clustering', 'transitivity', 'path_length', 'maximum_modularity']
x_order = list(zip([item for item in ('actual', 'control_mean', 'control_sd', 'actual_z') for _ in (0, 1)], ['ac', 'ww']*4))

data = json.load(open('/home/cbarnes/code/connectome/statistics/path_mod_cluster/path_cluster_phys_output.json', 'r'))

out_data = '\n'.join([','.join([str(data[source][stat][val_name]) for val_name, source in x_order]) for stat in y_order])

with open(path, 'w') as out_file:
    out_file.write(out_data)