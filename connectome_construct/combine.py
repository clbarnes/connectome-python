import construct_chklovskii as chk
import construct_emmons as emm
import node_data as dat
import add_extrasynaptic as extras
import networkx as nx


chkG = nx.MultiDiGraph()

chkG = chk.add_nodes(chkG)
nodelist = chk.get_nodelist(chkG)
chkG = chk.add_edges(chkG)
chkG = extras.add_extrasynaptic(chkG)
chkG = dat.add_all(chkG)

with open('/home/cbarnes/data/connectome/chklovskii/nodelist.txt', 'w') as data_file:
    data_file.write(','.join(nodelist))

nx.write_gpickle(chkG, '/home/cbarnes/data/connectome/chklovskii/gj-ma-np-syn_chk_herm.gpickle')

emmG = emm.G

emmG = extras.add_extrasynaptic(emmG)
emmG = dat.add_all(emmG)

nx.write_gpickle(emmG, '/home/cbarnes/data/connectome/emmons/gj-syn-ma-np_emm_herm.gpickle')