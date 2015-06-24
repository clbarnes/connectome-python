import networkx as nx
from multiplex import MultiplexConnectome
import community
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree
from scipy.spatial.distance import squareform
import sys

sys.setrecursionlimit(15000)

sources = ['ac', 'ww']
path_fstring = '/home/cbarnes/data/connectome/networks/{}_complete.gpickle'

C = {source: MultiplexConnectome(nx.read_gpickle(path_fstring.format(source))) for source in sources}

di_phys = {source: C[source].collapse('Synapse', 'GapJunction') for source in sources}

def collapse_to_undirected(di_graph):
    G = nx.Graph()
    G.add_nodes_from(di_graph.nodes())
    for src, tgt, data in di_graph.edges(data=True):
        if src == tgt:
            continue
        if src in G.edge and tgt in G.edge[src]:
            G.edge[src][tgt]['weight'] += data['summed_weight']
        else:
            G.add_edge(src, tgt, weight=data['summed_weight'])

    for node, degree in G.degree().items():
        if degree == 0:
            G.remove_node(node)

    return G


def make_linkage(G):
    if G.is_directed():
        G = collapse_to_undirected(G)
    nodelist = sorted(G.nodes())
    dist = np.array(nx.to_numpy_matrix(G, nodelist=nodelist))
    # dist[dist == 0] = 0.1
    np.fill_diagonal(dist, 0)
    dist = (np.max(dist) + 1) - dist
    np.fill_diagonal(dist, 0)
    lnk = linkage(squareform(dist))
    return lnk


def make_dendro(G, source='ww'):
    if G.is_directed():
        G = collapse_to_undirected(G)
    lnk = make_linkage(G)
    nodelist = sorted(G.nodes())
    for node in get_unconnected(G):
        nodelist.remove(node)
    if source == 'ww':
        dendrogram(lnk, labels=nodelist, color_threshold=158.5, )
    else:
        dendrogram(lnk, labels=nodelist)
        # plt.gca().set_ylim([80, 160])
    plt.xticks(rotation='vertical')
    plt.show()


def get_nodes(cluster_node):
    nodeset = set()

    if cluster_node is None:
        return set()
    if cluster_node.is_leaf():
        return {cluster_node.get_id()}
    else:
        nodeset.update(get_nodes(cluster_node.get_left()))
        nodeset.update(get_nodes(cluster_node.get_right()))

    return nodeset


def get_unconnected(G):
    return [component[0] for component in nx.connected_components(G) if len(component) == 1]


class TreeNode():
    def __init__(self, cluster_node, label_mapping=None, parent=None):
        if label_mapping is None:
            label_mapping = dict()
        self.label = label_mapping.get(cluster_node.get_id(), cluster_node.get_id())
        self.parent = parent
        self.children = self._populate(cluster_node, label_mapping)
        self.leaves = self._get_leaves()

    @staticmethod
    def from_linkage(lnk, label_mapping=None):
        if label_mapping is None:
            label_mapping = dict()

        cluster_node = to_tree(lnk)

        return TreeNode(cluster_node, label_mapping)


    @property
    def leaf_labels(self):
        return {leaf.label for leaf in self.leaves}

    @property
    def child_labels(self):
        return [child.label for child in self.children]

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return len(self.children) == 0

    def _populate(self, cluster_node, label_mapping):
        if cluster_node.is_leaf():
            return []
        else:
            return [TreeNode(cluster_node.get_left(), label_mapping, self),
                    TreeNode(cluster_node.get_right(), label_mapping, self)]

    def _get_leaves(self):
        ret = set()
        for child in self.children:
            if child.is_leaf():
                ret.add(child)
            else:
                ret.update(child.leaves)
        return ret

    @property
    def unrelated_leaf_labels(self):
        root = self.parent
        while not root.is_root():
            root = root.parent
        return root.leaf_labels

# make_linkage(di_phys['ac'])
source = 'ww'
make_dendro(di_phys[source], source)
#
# G = di_phys['ac']
# lnk = make_linkage(G)
#
# con_nodes = [node for node, degree in G.degree().items() if degree > 0]
# id_to_node = dict(enumerate(sorted(con_nodes)))
#
# tree = TreeNode.from_linkage(lnk, id_to_node)

pharyngeal = {line.strip() for line in open('/home/cbarnes/data/connectome/pharyngeal.txt', 'r').readlines()}

print('done')