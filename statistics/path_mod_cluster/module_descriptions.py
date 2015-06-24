#!/usr/bin/python2.7

import re
import json

descs = json.load(open('node_desc.json'))
add_mid_zero = re.compile(r'(?<=[A-Z])(?=\d$)')

source = 'ww'
etype = 'phys'
for source in ('ww', 'ac'):
    for etype in ('phys', 'ma'):
        modules = json.load(open('data/{}_{}_modules.json'.format(source, etype)))


        module_descs = []
        for module in modules:
            module_descs.append({node: descs[add_mid_zero.sub('0', node)] for node in module})

        json.dump(module_descs, open('data/{}_{}_module_descs.json'.format(source, etype), 'w'), sort_keys=True, indent=2)

print('done')