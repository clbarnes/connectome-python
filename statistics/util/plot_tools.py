from .data import order_by_time, order_by_nodes_born


def add_vlines_by_time(ax, label_height, fontdict=None):
    for name, x in order_by_time.items():
        ax.axvline(x=x, color='k', linestyle='--')
        ax.text(x=x+25, y=label_height, s=' ' + name, fontdict=fontdict, rotation='vertical')


def add_vlines_by_nodes_born(ax, label_height, fontdict=None):
    for name, x in order_by_nodes_born.items():
        ax.axvline(x=x, color='k', linestyle='--')
        ax.text(x=x + 1, y=label_height, s=' ' + name, fontdict=fontdict, rotation='vertical')


def pad_time_list(lst):
    """
    Return a timecourse extended to include 3000 (a timepoint just after maturity, in minutes) to the end of a list.

    :param lst: Time points in elegans development data
    :type lst: list
    :return: None
    """
    return lst + [3000]


def pad_y_list(lst):
    """
    Return a list padded with last value of the list to the list, in order_by_time to match up with a time list padded to reach maturity.

    :param lst: Dependent variable in elegans development data
    :type lst: list
    :return: None
    """
    return lst + [lst[-1]]