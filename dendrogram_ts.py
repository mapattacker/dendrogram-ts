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


def maxclust_draw(df, method, metric, max_cluster, ts_space=1):
    '''
    Description
    ------------
    Draw agglomerative clustering dendrogram based on maximum cluster criteron
    
    Arguments
    ---------
    df: dataframe or arrays of timeseries
    method: agglomerative clustering linkage method, e.g., 'ward'
    metric: distance metrics, e.g., 'euclidean'
    max_cluster: maximum cluster size to flatten cluster
    ts_space: horizontal space for timeseries graph to be plotted
    
    Output
    ------
    Plot dendrogram with timeseries graphs on the side
    '''
    
    # define gridspec space
    gs = gridspec.GridSpec(max_cluster,max_cluster)

    # add dendrogram to gridspec
    plt.subplot(gs[:, 0:max_cluster-ts_space])
    plt.xlabel('Distance')
    plt.ylabel('Cluster')

    # agglomerative clustering
    Z = linkage(df, method=method, metric=metric)
    ddata = dendrogram(Z, orientation='left',
                       truncate_mode='lastp', p=max_cluster,
                       labels=True, get_leaves=True,
                       show_leaf_counts=True,
                       show_contracted=True)
    
    # add distance labels in dendrogram
    add_distance(ddata)            

    # get cluster labels
    y = fcluster(Z, max_cluster, criterion='maxclust')
    y = pd.DataFrame(y,columns=['y'])

    # merge with original dataset
    dx=pd.concat([df.reset_index(drop=True), y],axis=1)

    # add timeseries graphs to gridspec
    for cluster in range(1,max_cluster+1):
        reverse_plot = max_cluster+1-cluster
        plt.subplot(gs[reverse_plot-1:reverse_plot,max_cluster-ts_space:max_cluster])
        plt.axis('off')
        for i in range(len(dx[dx['y']==cluster])):
            plt.plot(dx[dx['y']==cluster].T[:-1].iloc[:,i]);

    plt.tight_layout()

