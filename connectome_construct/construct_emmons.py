import xlrd
import networkx as nx

syn_path = '/home/cbarnes/data/connectome/emmons/hermaphrodite chemical.xlsx'
gj_path = '/home/cbarnes/data/connectome/emmons/hermaphrodite gj.xlsx'

others = {'hyp', 'intestine', 'intL', 'intR', 'sph', 'anal'}

G = nx.MultiDiGraph()


def get_gj(graph=G, path=gj_path):
    G = graph.copy()
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_index(0)
    labels = []
    label = ''
    for j, cell in enumerate(worksheet.row(0)):
        if j == 0:
            labels.append(None)
            continue
        elif j >= worksheet.ncols - 2:
            break

        if cell.ctype != 0:
            label = cell.value.strip()

        labels.append(cell.value.strip() if cell.value.strip() else label)

    tgts = []
    for j, cell in enumerate(worksheet.row(1)):
        if j == 0:
            tgts.append(None)
            continue
        elif not cell.ctype:
            break

        val = cell.value.strip()

        tgts.append(val)
        if cell.value:
            label = 'other' if val in others else labels[j]
            G.add_node(val, label=label, neuron='neuron' in label)

    for row in (worksheet.row(val) for val in range(worksheet.nrows - 1)):
        if not row[0].ctype:
            continue
        else:
            src = row[0].value
        for j, cell in enumerate(row[1:], 1):
            if j > len(tgts)-1:
                break
            if cell.ctype == 2:
                weight = cell.value
                G.add_edge(src, tgts[j], weight=weight, type='GapJunction')

    return G


def get_syn(graph=G, path=syn_path):
    G = graph.copy()
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_index(0)
    tgts = []
    for j, cell in enumerate(worksheet.row(0)):
        if j == 0:
            tgts.append(None)
            continue
        elif not cell.ctype:
            break

        tgts.append(cell.value.strip())

    for row in (worksheet.row(val) for val in range(worksheet.nrows - 1)):
        if not row[0].ctype:
            continue
        else:
            src = row[0].value.strip()
        for j, cell in enumerate(row[1:], 1):
            if j > len(tgts)-1:
                break
            if cell.ctype == 2:
                weight = cell.value
                G.add_edge(src, tgts[j], weight=weight, type='Synapse')

    return G


G = get_gj(G)
G = get_syn(G)

