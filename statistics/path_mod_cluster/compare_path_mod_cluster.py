from matplotlib import pyplot as plt
import json
import numpy as np

plt.style.use('ggplot')

data = {'phys': json.load(open('path_cluster_phys_output.json')),
        'ma': json.load(open('path_cluster_ma_output.json'))}


fig, axes_arr = plt.subplots(2, 2)

metrics = ['path_length', 'clustering', 'maximum_modularity', 'transitivity']

def plot_metric(ax, metric):
    n = 2
    ind = np.arange(n)
    width = 0.3

    xlabels = ['AC', 'WW']
    # xlabels = ['AC\nphys', 'AC\nphys+ma', 'WW\nphys', 'WW\nphys+ma']
    # legend = ['Physical', 'Including MA', 'C. elegans']

    phys_mean = [data['phys']['ac'][metric]['control_mean'], data['phys']['ww'][metric]['control_mean']]
    phys_err = [data['phys']['ac'][metric]['control_sd'], data['phys']['ww'][metric]['control_sd']]
    phys_actual = [data['phys']['ac'][metric]['actual'], data['phys']['ww'][metric]['actual']]

    ma_mean = [data['ma']['ac'][metric]['control_mean'], data['ma']['ww'][metric]['control_mean']]
    ma_err = [data['ma']['ac'][metric]['control_sd'], data['ma']['ww'][metric]['control_sd']]
    ma_actual = [data['ma']['ac'][metric]['actual'], data['ma']['ww'][metric]['actual']]

    phys_bar = ax.bar(ind, phys_mean, width, color='c', alpha=0.3, yerr=phys_err, error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))
    ma_bar = ax.bar(ind+width, ma_mean, width, color='m', alpha=0.3, yerr=ma_err, error_kw=dict(ecolor='gray', lw=2, capsize=5, capthick=2))

    phys_x = ind + width * 0.5
    ma_x = ind + width*1.5

    phys_scatter = ax.scatter(phys_x, phys_actual, marker='d', color='c', s=30)
    ma_scatter = ax.scatter(ma_x, ma_actual, marker='d', color='m', s=30)

    ax.set_ylabel(metric)
    # ax.set_xticks(sorted(np.concatenate((phys_x, ma_x))))
    ax.set_xticks(ind+width)
    ax.set_xticklabels(xlabels)
    ax.set_ylim(bottom=0)

    return phys_bar, ma_bar, phys_scatter, ma_scatter

for ax, metric in zip(list(axes_arr.flatten()), metrics):
    hndls = plot_metric(ax, metric)

fig.subplots_adjust(bottom=0.18)

legend_labels = ('Randomised physical', 'Randomised physical and monoamine', 'C. elegans physical', 'C. elegans physical and monoamine')

plt.legend(hndls, legend_labels, loc='lower center', bbox_to_anchor = (0,0.02,1,1),
            bbox_transform=plt.gcf().transFigure, borderaxespad=0.)

plt.show()