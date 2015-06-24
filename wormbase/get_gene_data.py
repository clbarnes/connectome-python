import requests
import re
import networkx as nx
import progressbar as pb
import json
import pandas as pd
import warnings

df = pd.DataFrame.from_csv('expression_data.csv')

genes = list(df)

wb_id_re = re.compile('c_elegans/gene/(WBGene\d*)')

def get_wbid(name):
    name_search_url = 'http://www.wormbase.org/search/gene/{}'
    response = requests.get(name_search_url.format(name))
    return wb_id_re.search(response.url).groups()[0]


def get_description(wbid):
    query_url = 'http://api.wormbase.org/rest/field/gene/{}/concise_description'.format(wbid)
    data = requests.get(query_url, headers={'Content-Type': 'application/json'}).json()

    return data['concise_description']['data']['text']

pbar = pb.ProgressBar(maxval=len(genes), widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()

gene_descriptions = dict()
count = 0
for gene in genes:
    wbid = get_wbid(gene)
    desc = get_description(wbid)
    gene_descriptions[gene] = desc
    count += 1
    pbar.update(count)

json.dump(gene_descriptions, open('gene_descriptions.json', 'w'), indent=4, sort_keys=True)

print('done')