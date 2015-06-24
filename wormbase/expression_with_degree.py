from multiplex import MultiplexConnectome
import networkx as nx
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
import json
import progressbar as pb


pretty_json = {'sort_keys': True, 'indent': 4, 'separators': (',', ': ')}


def cross_validate(X, y, n_folds=10):
    kf = KFold(len(y), n_folds=n_folds, shuffle=True)
    rmse = []
    for train_inds, test_inds in kf:
        X_train, X_test = X.values[train_inds], X.values[test_inds]
        y_train, y_test = y[train_inds], y[test_inds]

        las = Lasso(max_iter=5000)

        las.fit(X_train, y_train)

        y_pred = las.predict(X_test)

        rmse.append(np.sqrt(mean_squared_error(y_test, y_pred)))

    return np.mean(rmse)

ww = MultiplexConnectome(nx.read_gpickle('/home/cbarnes/data/connectome/networks/ww_complete.gpickle'))
df = pd.DataFrame.from_csv('expression_data.csv')
X = df
nodelist = list(df.index)


def mean_shortest_path_length(graph, nodes):
    spl = nx.shortest_path_length(graph)
    return {src: np.mean(list(spl[src].values())) for src in spl}


def clustering(graph, nodes):
    G = nx.Graph(graph)
    return nx.clustering(G, nodes)


def triangles(graph, nodes):
    G = nx.Graph(graph)
    return nx.triangles(G, nodes)

algos = {'degree': nx.degree, 'triangles': triangles, 'clustering': clustering, 'shortest_path': mean_shortest_path_length}
pbar = pb.ProgressBar(maxval=len(algos)*len(ww.sub), widgets=[pb.Percentage(), pb.Bar(), pb.ETA()]).start()

results = {key: dict() for key in algos}
count = 0
for algo, fn in algos.items():
    rmse = dict()
    weights = dict()
    sds = dict()
    for name in ww.sub:
        d = fn(ww[name], ww[name].nodes())
        y = np.array([d[node] for node in nodelist])
        sds[name] = np.std(y)

        rmse[name] = cross_validate(X, y)

        las = Lasso(max_iter=5000)
        las.fit(X, y)
        weights[name] = {gene: coeff for gene, coeff in zip(df, las.coef_) if abs(coeff) > 0.0001}
        count += 1
        pbar.update(count)

    results[algo]['sds'] = sds
    results[algo]['rmse'] = rmse
    results[algo]['weights'] = weights

out = {'nodelist': nodelist, 'results': results}

json.dump(out, open('expression_graph_correlation.json', 'w'), **pretty_json)

print('\ndone')