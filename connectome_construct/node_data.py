from urllib import request
from bs4 import BeautifulSoup
from string import digits
import re

edge_birthtime_path = '/home/cbarnes/data/connectome/birthtime_location.csv'
wormatlas_path = '/home/cbarnes/data/connectome/worm_atlas_cell_data.psv'


def add_pos_birthtime(G):
    G = G.copy()

    with open(edge_birthtime_path, 'r') as data_file:
        next(data_file)
        node_data = dict()
        for row in data_file:
            cell, birthtime, x, y = row.strip().split(',')
            node_data[cell] = {'birthtime': birthtime, 'position': (float(x), float(y))}

    for node, data in G.nodes_iter(data=True):
        data.update(node_data.get(node, {'birthtime': None, 'position': None}))

    return G


def add_wormatlas_data(G):
    G = G.copy()

    node_data = dict()
    with open(wormatlas_path, 'r') as data_file:
        for row in data_file:
            node, lineage, description = row.strip().split('|')
            node_data[node] = {'lineage': lineage, 'description': description}

    for node, data in G.nodes_iter(data=True):
        if node not in node_data:
            data.update({'lineage': '', 'description': '', 'type': ''})
            continue

        data.update(node_data[node])

        if 'interneuron' in data['description'].lower():
            data['type'] = 'interneuron'
        elif 'motor' in data['description'].lower():
            data['type'] = 'motor'
        elif 'sensory' in data['description'].lower() or 'receptor' in data['description'].lower():
            data['type'] = 'sensory'
        elif 'neuron' in data['description'].lower():
            data['type'] = 'interneuron'
        elif 'muscle' in data['description'].lower():
            data['type'] = 'muscle'

    return G


def clean_line(line):
    return ' '.join(line.strip().split())


def scrape_data(name):
    link = 'http://www.wormatlas.org/neurons/Individual%20Neurons/{}mainframe.htm'.format(name)
    url = request.urlopen(link).read()
    soup = BeautifulSoup(url)
    tables = soup.find_all('table')[4:6]
    headings = [strong.text.strip() for strong in tables[0].find_all('strong') + tables[1].find_all('strong')
                if ':' in strong.text]
    data_str = '\n'.join([tables[0].text, tables[1].text])
    data = dict()
    for start_head, end_head in zip(headings, headings[1:]):
        start_ind = data_str.index(start_head) + len(start_head)
        end_ind = data_str.index(end_head)
        data[start_head] = data_str[start_ind:end_ind]
    data[end_head] = data_str[end_ind + len(end_head):]


    cleaned_data = dict()
    for key, value in data.items():
        new_key = 'wa_' + key.strip()[:-1].lower()
        new_value = ' '.join(value.strip().split()).strip()
        new_value = '\n- '.join(new_value.split(' - '))
        cleaned_data[new_key] = new_value

    return cleaned_data


def get_name_to_url():
    link = 'http://www.wormatlas.org/neurons/Individual%20Neurons/neuronsmainframe.htm'
    url = request.urlopen(link).read()
    soup = BeautifulSoup(url)
    table = soup.find_all('table')[4]
    all_a = table.find_all('a')
    d = {tag.text: tag['href'][:-13] for tag in all_a}

    additional = dict()

    for key, value in d.items():
        if '/' in key:
            additional[key[:-2]] = value
            additional[key[:-3] + key[-1]] = value

    d.update(additional)

    additional = dict()

    for key, value in d.items():
        if key.startswith('DA'):
            additional[key] = 'DAN'
        elif key.startswith('DB'):
            additional[key] = 'DBN'
        elif key.startswith('DD'):
            additional[key] = 'DDN'
        elif key.startswith('VA'):
            additional[key] = 'VAN'
        elif key.startswith('VB'):
            additional[key] = 'VBN'
        elif key.startswith('VC'):
            additional[key] = 'VCN'
        elif key.startswith('VD'):
            additional[key] = 'VDN'
        elif key.startswith('AS'):
            additional[key] = 'ASN'

    d.update(additional)

    return d

def add_scraped_data(G):
    G = G.copy()

    name_to_url = get_name_to_url()

    regex = re.compile('(.+)0(\d+)')

    i = 0
    number = len(G.nodes())

    for node, data in G.nodes_iter(data=True):
        i += 1
        print('Getting node data: {} of {}'.format(i, number))

        search = regex.search(node)
        node_name = ''.join(search.groups()) if search else node


        data.update(scrape_data(name_to_url[node_name]))

        if 'interneuron' in data['wa_type'].lower():
            data['type'] = 'interneuron'
        elif 'motor' in data['wa_type'].lower():
            data['type'] = 'motor'
        elif 'sensory' in data['wa_type'].lower():
            data['type'] = 'sensory'
        else:
            data['type'] = 'interneuron'

    return G


def add_all(G):
    G = G.copy()
    G = add_pos_birthtime(G)
    G = add_scraped_data(G)
    return G
