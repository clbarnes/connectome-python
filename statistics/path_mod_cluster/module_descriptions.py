#!/usr/bin/python2.7

import re
import json
import progressbar as pb
import random as rand
from itertools import chain
from collections import Counter, defaultdict
from scipy.stats import binom



descs = json.load(open('node_desc.json'))

source = 'ww'
etype = 'phys'
modules = json.load(open('data/{}_{}_modules.json'.format(source, etype)))

non_letters = re.compile(r'\.|,|\(|\)|:|;')


def desc_to_bag(s):
    s = non_letters.sub('', s)
    s.replace(u'/', ' ')
    s = s.lower()
    s = s.split()

    return set(s)


word_probs = defaultdict(float)
all_bags = {key: desc_to_bag(desc) for key, desc in descs.items()}
for bag in all_bags.values():
    for word in bag:
        word_probs[word] += 1.0/float(len(all_bags))

add_mid_zero = re.compile(r'(?<=[A-Z])(?=\d$)')

def module_to_wordlist(module):
    lst = []
    for node in module:
        lst.extend(all_bags[add_mid_zero.sub('0', node)])
    return lst


module_words = []
for module in modules:
    wordlist = module_to_wordlist(module)
    words_pvals = dict()
    for word, count in Counter(wordlist).items():
        words_pvals[word] = binom.sf(count - 1, len(module), word_probs[word])
    module_words.append({word: pval for word, pval in words_pvals.items() if pval < 0.01})

print('done')