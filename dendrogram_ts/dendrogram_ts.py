import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage


def add_distance(ddata, dist_threshold=None, fontsize=8):
    """Plot cluster points & distance labels in dendrogram

    Args
        ddata (np array): scipy dendrogram output
        dist_threshold: distance threshold where label will be drawn,
                        if None, 1/10 from base leafs will not be labelled to prevent clutter
        fontsize (int): size of distance labels
    """

    if dist_threshold is None:
        # add labels except for 1/10 from base leaf nodes
        dist_threshold = max([a for i in ddata["dcoord"] for a in i]) / 10
    for i, d, c in zip(ddata["icoord"], ddata["dcoord"], ddata["color_list"]):
        y = sum(i[1:3]) / 2
        x = d[1]

        # space labels to right so does not touch the nodes
        label_len = len(str(int(x)))
        if label_len > 5:
            rspace = label_len - 1
        else: 
            rspace = 0
        
        # only label above distance threshold
        if x > dist_threshold:
            plt.plot(x, y, "o", c=c, markeredgewidth=0)
            plt.annotate(
                int(x),
                (x, y),
                xytext=(15+rspace, 3),
                textcoords="offset points",
                va="top",
                ha="center",
                fontsize=fontsize,
            )


def draw_timeseries(dx, max_cluster, gs, ts_hspace, clustcolor=None):
    """plot timeseries graphs beside dendrogram"""

    for cluster in range(1, max_cluster + 1):
        reverse_plot = max_cluster + 1 - cluster
        plt.subplot(
            gs[reverse_plot - 1 : reverse_plot, max_cluster - ts_hspace : max_cluster]
        )
        plt.axis("off")
        for i in range(len(dx[dx["y"] == cluster])):
            if clustcolor:
                color = clustcolor[cluster - 1]
                plt.plot(dx[dx["y"] == cluster].T[:-1].iloc[:, i], color=color)
            else:
                plt.plot(dx[dx["y"] == cluster].T[:-1].iloc[:, i])


def maxclust_draw(df, method, metric, max_cluster, ts_hspace=1, dist_label=False):
    """Draw agglomerative clustering dendrogram with timeseries graphs based on maximum cluster criteron

    Args
        df (pd dataframe): df with each row being the time window of readings
        method: agglomerative clustering linkage method, e.g., 'ward'
        metric: distance metrics, e.g., 'euclidean'
        max_cluster: maximum cluster size to trim dendrogram, and extract cluster labels
        ts_hspace: horizontal space for timeseries graph to be plotted

    Out
        Plot dendrogram with aggregrated timeseries graphs on the side
        based on maximum cluster
    """

    # define gridspec space
    gs = gridspec.GridSpec(max_cluster, max_cluster)

    # add dendrogram to gridspec
    plt.subplot(gs[:, 0 : max_cluster - ts_hspace])
    plt.xlabel("Distance")
    plt.ylabel("Cluster")

    # agglomerative clustering
    Z = linkage(df, method=method, metric=metric)
    ddata = dendrogram(
        Z,
        orientation="left",
        truncate_mode="lastp",
        p=max_cluster,
        get_leaves=True,
        show_leaf_counts=True,
        show_contracted=True,
    )

    # add distance labels in dendrogram
    if dist_label:
        add_distance(ddata)

    # get cluster labels
    y = fcluster(Z, max_cluster, criterion="maxclust")
    y = pd.DataFrame(y, columns=["y"])

    # merge with original dataset
    dx = pd.concat([df.reset_index(drop=True), y], axis=1)

    # add timeseries graphs to gridspec
    draw_timeseries(dx, max_cluster, gs, ts_hspace)

    plt.tight_layout()
    return dx


def allclust_draw(df, method, metric, ts_hspace=2, dist_label=False):
    """
    Draw agglomerative clustering dendrogram with timeseries graphs for all clusters

    Args
        df (pd dataframe): df with each row being the time window of readings
        method (str): agglomerative clustering linkage method, e.g., 'ward'
        metric (str): distance metrics, e.g., 'euclidean'
        ts_hspace (int): horizontal space for timeseries graph to be plotted

    Out
        Plot dendrogram with all timeseries graphs on the side when distance=0
    """

    # agglomerative clustering
    Z = linkage(df, method=method, metric=metric)
    max_cluster = len(Z) + 1

    # define gridspec space
    gs = gridspec.GridSpec(max_cluster, max_cluster)

    # add dendrogram to gridspec
    # add -1 to give timeseries graphs more space
    plt.subplot(gs[:, 0 : max_cluster - ts_hspace - 1])
    plt.xlabel("Distance")
    plt.ylabel("Cluster")

    ddata = dendrogram(Z, orientation="left", show_leaf_counts=True)

    # add distance labels in dendrogram
    if dist_label:
        add_distance(ddata)

    # get all cluster labels by inputting distance 0 threshold
    y = fcluster(Z, 0, criterion="distance")
    y = pd.DataFrame(y, columns=["y"])

    # merge with original dataset
    dx = pd.concat([df.reset_index(drop=True), y], axis=1)

    # add timeseries graphs to gridspec
    draw_timeseries(dx, max_cluster, gs, ts_hspace)

    # removed as kept having error when there are many clusters
    # plt.tight_layout() 


def colorclust_draw(df, method, metric, color_threshold, ts_hspace=1, dist_label=False):
    """
    Draw agglomerative clustering dendrogram with timeseries graphs for cluster threshold by color

    Args
        df (pd dataframe): df with each row being the time window of readings
        method: agglomerative clustering linkage method, e.g., 'ward'
        metric: distance metrics, e.g., 'euclidean'
        color_threshold: plot dendrogram cluster colors using a distance threshold
        ts_hspace: horizontal space for timeseries graph to be plotted

    Out
        Plot dendrogram with timeseries graphs classified by color on the side
    """

    # agglomerative clustering
    Z = linkage(df, method=method, metric=metric)

    # get cluster size via no. unique colors from color threshold
    clustcolor = dendrogram(Z, color_threshold=color_threshold, no_plot=True)[
        "color_list"
    ]
    clustcolor = np.array(clustcolor)
    # arrange colors to order after np.unique
    _, idx = np.unique(clustcolor, return_index=True)
    clustcolor = clustcolor[np.sort(idx)]
    # remove additional blue base linkage color
    clustcolor = [i for i in clustcolor if i != "b"]

    # get all cluster labels by inputting distance using color_threshold
    y = fcluster(Z, color_threshold, criterion="distance")
    max_cluster = max(y)
    y = pd.DataFrame(y, columns=["y"])

    # define gridspec space
    gs = gridspec.GridSpec(max_cluster, max_cluster)

    # add dendrogram to gridspec
    plt.subplot(gs[:, 0 : max_cluster - ts_hspace])
    plt.xlabel("Distance")
    plt.ylabel("Cluster")
    plt.axis("off")

    ddata = dendrogram(
        Z,
        orientation="left",
        color_threshold=color_threshold,
        show_leaf_counts=True
    )

    # add distance labels in dendrogram
    if dist_label:
        add_distance(ddata)

    # add distance cutoff line
    line = color_threshold
    plt.axvline(x=line, c="black", lw=0.5, linestyle="--")

    # merge with original dataset
    dx = pd.concat([df.reset_index(drop=True), y], axis=1)

    # add timeseries graphs to gridspec
    draw_timeseries(dx, max_cluster, gs, ts_hspace, clustcolor=clustcolor)

    plt.tight_layout()
