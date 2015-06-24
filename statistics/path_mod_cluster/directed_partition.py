import networkx as nx
from multiplex import MultiplexConnectome
from collections import OrderedDict
import progressbar as pb
import graph_tool as gt
from graph_tool import centrality
import json

sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

data_root = '/home/cbarnes/data/connectomes'

G = C['ac'].collapse('GapJunction', 'Synapse')


def invert_weight(G):
    graph = G.copy()
    max_weight = max(nx.get_edge_attributes(graph, 'summed_weight').values()) + 1
    for _, _2, data in G.edges_iter(data=True):
        data['summed_weight'] = max_weight - data['summed_weight']

    return graph

G_inv = invert_weight(G)


def betweenest_edge(G, value=False):
    edge, betweenness = max(
        nx.edge_betweenness_centrality(G, weight='summed_weight').items(),
        key=lambda item: item[1]
    )

    return edge, betweenness if value else edge


def remove_edges_by_betweenness(G, cutoff=0):
    graph = G.copy()
    betweenest = OrderedDict()
    starting_edges = graph.number_of_edges()
    pbar = pb.ProgressBar(maxval=starting_edges, widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()
    while graph.number_of_edges():
        edge, bet_value = betweenest_edge(graph, value=True)
        if bet_value < cutoff:
            break
        betweenest[edge] = bet_value
        graph.remove_edge(*edge)
        pbar.update(starting_edges - graph.number_of_edges())

    return betweenest


def nx_to_gt(nxg):
    gtg = gt.Graph()
    int_to_name = dict(enumerate(sorted(nxg.nodes_iter())))
    name_to_int = {value: key for key, value in int_to_name.items()}
    gtg.add_edge_list([(name_to_int[src], name_to_int[tgt]) for src, tgt in nxg.edges_iter()])
    gtg.edge_properties['weight'] = gtg.new_edge_property('int')
    gtg.vertex_properties['name'] = gtg.new_vertex_property('string')

    for edge in gtg.edges():
        src_int, tgt_int = int(edge.source()), int(edge.target())
        gtg.edge_properties['weight'][edge] = nxg[int_to_name[src_int]][int_to_name[tgt_int]]['summed_weight']

    for vertex in gtg.vertices():
        gtg.vertex_properties['name'][vertex] = int_to_name[int(vertex)]

    return gtg


def betweenest_edge_gt(gtg, value=False):
    ebc = centrality.betweenness(gtg, weight=gtg.edge_properties['weight'])[1]
    highest_bet = ebc.a.max()

    for edge in gtg.edges():
        if ebc[edge] == highest_bet:
            return edge, highest_bet if value else edge


def remove_edges_by_betweenness_gt(gtg, cutoff=0):
    graph = gtg.copy()
    betweenest = OrderedDict()
    starting_edges = graph.num_edges()
    pbar = pb.ProgressBar(maxval=starting_edges, widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()
    while graph.num_edges():
        edge, bet_value = betweenest_edge_gt(graph, value=True)
        if bet_value < cutoff:
            break

        src, tgt = int(edge.source()), int(edge.target())
        betweenest[(src, tgt)] = bet_value
        graph.remove_edge(edge)
        pbar.update(starting_edges - graph.num_edges())

    return betweenest


print('starting')

# betweenest = remove_edges_by_betweenness(G)

int_to_name = dict(enumerate(sorted(G_inv.nodes_iter())))
gtg = nx_to_gt(G_inv)

raw_betweenest = remove_edges_by_betweenness_gt(gtg)

betweenest = [[[int_to_name[src], int_to_name[tgt]], float(value)]
                         for (src, tgt), value in raw_betweenest.items()]

json.dump(betweenest, open('ac_betweenest_order.json', 'w'), indent=4)

print('done')