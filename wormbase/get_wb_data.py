import requests
import re
import networkx as nx
import progressbar as pb
import json
import pandas as pd
import warnings


ww = nx.read_gpickle('/home/cbarnes/data/connectome/networks/ww_complete.gpickle')

name_search_url = 'http://www.wormbase.org/db/ontology/anatomy?name={}'
expr_url = 'http://api.wormbase.org/rest/field/anatomy_term/{}/expression_patterns'
desc_url = 'http://api.wormbase.org/rest/field/anatomy_term/{}/definition'
wb_id_re = re.compile('anatomy_term/(.*?)\?from=')
mid_0_re = re.compile('(?<=[A-Z])(0)(?=\d)')


def get_wbid(name):
    clean_name = mid_0_re.sub('', name)

    for query in (clean_name, clean_name + ' neuron'):
        response = requests.get(name_search_url.format(query))
        wbid = wb_id_re.search(response.url).groups()[0]
        if 'WBbt:' in wbid:
            return wbid

    warnings.warn('Could not find wbid for name {}.'.format(clean_name))
    return None


def get_wbids(graph):
    pbar = pb.ProgressBar(maxval=graph.number_of_nodes(), widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()
    data = dict()
    for i, node in enumerate(graph.nodes_iter()):
        pbar.update(i)
        data[node] = {'wbid': get_wbid(node)}

    return data


def get_expression(wbid):
    if wbid == 'WBbt:0004868':
        wbid = 'WBbt:0005339'
    url = expr_url.format(wbid)
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'}).json()
        assert(type(response['expression_patterns']['data']) == list)
    except (ValueError, AssertionError) as e:
        raise ValueError('{} is borked'.format(wbid), e)
    return [item['gene']['label'] for item in response['expression_patterns']['data'] if item['gene']]


def get_description(wbid):
    if wbid == 'WBbt:0004868':
        wbid = 'WBbt:0005339'
    url = desc_url.format(wbid)
    try:
        response = requests.get(url, headers={'Content-Type': 'application/json'}).json()
        # assert(type(response['expression_patterns']['data']) == list)
    except (ValueError, AssertionError) as e:
        warnings.warn('{} is borked'.format(wbid), e)
        return ''
    return response['definition']['data']


def get_expressions(data):
    pbar = pb.ProgressBar(maxval=ww.number_of_nodes(), widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()
    for i, (name, d) in enumerate(data.items()):
        pbar.update(i)
        d['expression'] = get_expression(d['wbid'])


def dict_to_sparse(data):
    dumb_df = pd.DataFrame.from_dict({'gene_expression': {name: d['expression'] for name, d in data.items()}})
    return dumb_df['gene_expression'].str.join(sep='*').str.get_dummies(sep='*')


#data = get_wbids(ww)

data = json.load(open('data_file.json', 'r'))
#json.dump(data, open('data_file.json', 'w'))

# descs = {name: get_description(value['wbid']) for name, value in data.items()}
descs = json.load(open('descriptions.json', 'r'))
json.dump(descs, open('descriptions.json', 'w'), indent=2, sort_keys=True)

# json.dump(data, open('data_file.json', 'w'))
#
# df = dict_to_sparse(data)
#
# df

print('done')