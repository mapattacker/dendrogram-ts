import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def add_distance(ddata, dist_threshold=None, fontsize=8):
    '''
    Description
    ------------
    Plot cluster points & distance labels in dendrogram

    Arguments
    ---------
    ddata: scipy dendrogram output
    dist_threshold: distance threshold where label will be drawn, if None, 1/10 from base leafs will not be labelled to prevent clustter
    fontsize: size of distance labels
    '''
    if dist_threshold==None:
        # add labels except for 1/10 from base leaf nodes
        dist_threshold = max([a for i in ddata['dcoord'] for a in i])/10
    for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
        y = sum(i[1:3])/2
        x = d[1]
        # only label above distance threshold
        if x > dist_threshold:
            plt.plot(x, y, 'o', c=c, markeredgewidth=0)
            plt.annotate(int(x), (x, y), xytext=(15, 3),
                         textcoords='offset points',
                         va='top', ha='center', fontsize=fontsize)