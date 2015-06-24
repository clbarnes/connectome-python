"""
In this example an axon is built, a morphology is loaded, the axon is
then connected to the loadeed morphology.
"""

import neuroml.loaders as loaders
import os
import networkx as nx
from multiplex import MultiplexConnectome
from collections import namedtuple
import numpy as np
import re
import json


SegmentDimensions = namedtuple('SegmentDimensions', ['x', 'y', 'z', 'diameter'])


def plane_to_segmentdimensions(plane):
    return SegmentDimensions(plane.x, plane.y, plane.z, plane.diameter)


def doc_to_segmentdimensions(path):
    doc = loaders.NeuroMLLoader.load(path)
    neurone = []
    soma = []
    for seg in doc.cells[0].morphology.segments:
        if 'soma' in seg.name.lower():
            soma = (seg.proximal.x, seg.proximal.y, seg.proximal.z)

        try:
            neurone.append(plane_to_segmentdimensions(seg.proximal))
        except AttributeError:
            pass

        try:
            neurone.append(plane_to_segmentdimensions(seg.distal))
        except AttributeError:
            pass

    arr = np.array(neurone)[:, :-1]
    mins = np.amin(arr, 0)
    maxes = np.amax(arr, 0)

    return {'soma': soma, 'neurone': neurone, 'bounds': list(list(item) for item in zip(mins, maxes))}


ww = MultiplexConnectome(nx.read_gpickle('/home/cbarnes/data/connectome/networks/ww_complete.gpickle'))
morph_root = '/home/cbarnes/data/connectome/CElegansNeuroML/CElegans/generatedNeuroML2'

mid_0_re = re.compile('(?<=[A-Z])(0)(?=\d)')

node_morphs = dict()

for node in ww.whole.nodes_iter():
    path = os.path.join(morph_root, '{}.nml'.format(mid_0_re.sub('', node)))
    node_morphs[node] = doc_to_segmentdimensions(path)

json.dump(node_morphs, open('morphologies.json', 'w'), indent=4, sort_keys=True)

print('done')