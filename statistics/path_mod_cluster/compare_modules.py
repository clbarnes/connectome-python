import networkx as nx
from multiplex import MultiplexConnectome
import subprocess as sp
from random import random
import re
import os
from collections import defaultdict
import json

sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

di_phys = {source: C[source].compose('Synapse', 'GapJunction') for source in sources}
undi_phys = {source: nx.Graph(di_phys[source]) for source in sources}


def write_linklist(G, output_path, weight_attr='weight'):
    nodelist = sorted(G.nodes())
    node_to_int = {node: i for i, node in enumerate(nodelist, 1)}

    with open(output_path, 'w') as f:
        f.writelines('#{} {}\n'.format(node_to_int[node], node) for node in nodelist)
        f.writelines('{} {} {}\n'.format(node_to_int[src], node_to_int[tgt], data.get(weight_attr, 1))
                     for src, tgt, data in G.edges_iter(data=True))


def write_pajek(G, output_path, weight_attr='weight'):
    nodelist = sorted(G.nodes())
    node_to_int = {node: i for i, node in enumerate(nodelist, 1)}

    with open(output_path, 'w') as f:
        f.write('*Vertices {}\n'.format(G.number_of_nodes()))
        f.writelines('{} "{}" 1.0\n'.format(node_to_int[node], node) for node in nodelist)
        f.write('*Arcs {}\n'.format(G.number_of_edges()))
        f.writelines('{} {} {}\n'.format(node_to_int[src], node_to_int[tgt], data.get(weight_attr, 1))
                     for src, tgt, data in G.edges_iter(data=True))


def write_smap(G, out_file_root='tmp', random_seed=None):
    infomap_path = '/home/cbarnes/code/lib/conf-infomap_dir/conf-infomap'
    tmp_path = '{}.net'.format(out_file_root)
    if random_seed is None:
        random_seed = round(random()*1000000)

    write_pajek(G, tmp_path, 'summed_weight')
    sp.call([infomap_path, str(random_seed), tmp_path, str(10), str(100), str(0.90)])


def smap_to_modules(smap_path):
    regex = re.compile(r'^(\d+)(;|:)\d+\s"(\w+)"\s(0\.\d+)$')
    with open(smap_path, 'r') as f:
        lines = [s.strip() for s in f.readlines()]

    modules = defaultdict(dict)

    for line in lines:
        result = regex.search(line)
        if result:
            g = result.groups()
            modules[int(g[0])][g[2]] = float(g[3])

    modules = [modules[key] for key in sorted(modules.keys(), key=lambda x: len(modules[x]), reverse=True)]

    json.dump(modules, open(smap_path[:-5] + '_modules.json', 'w'), indent=2, sort_keys=True)


def main():
    for source in ('ww', 'ac'):
        for etype in ('phys', 'ma'):
            if etype == 'ma':
                G = C[source].compose('GapJunction', 'Synapse', 'Monoamine')
            else:
                G = C[source].compose('GapJunction', 'Synapse')
            write_smap(G, 'data/{}_{}'.format(source, etype), 1)
            smap_to_modules('data/{}_{}.smap'.format(source, etype))

    print('\n\nfinished\n')

if __name__ == '__main__':
    main()
