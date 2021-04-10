Dendrogram Timeseries
=====================

Scipy's dendrogram for agglomerative clustering requires extensive customizations
to make it more informative. This package wraps scipy's dendrogram with two customizations:

    * Timeseries graph at the side
    * Distance labels and cluster split points
 

Installation
------------

.. code:: bash
    
    pip install dendrogram_ts

Example
-------

Plot by Maximum Clusters
************************

.. code:: python

    from dendrogram_ts import maxclust_draw

    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(8,5));

    maxclust_draw(df, 'ward', 'euclidean', max_cluster=10, ts_hspace=2)


.. figure:: https://github.com/mapattacker/dendrogram-ts/blob/master/images/dendrogram1.png
    :width: 650px
    :align: center

Plot by Color Threshold
***********************

.. code:: python

    from dendrogram_ts import colorclust_draw
    import matplotlib as mpl

    mpl.rcParams['lines.linewidth'] = 1
    plt.style.use('seaborn-white')
    plt.figure(figsize=(12,10))

    colorclust_draw(df, method='ward', metric='euclidean', color_threshold=5200, ts_hspace=1)

.. figure:: https://github.com/mapattacker/dendrogram-ts/blob/master/images/dendrogram3.png
    :width: 650px
    :align: center

Plot All Clusters
*****************

.. code:: python

    from dendrogram_ts import allclust_draw

    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(12,10))

    allclust_draw(df, 'ward', 'euclidean', ts_hspace=5)

.. figure:: https://github.com/mapattacker/dendrogram-ts/blob/master/images/dendrogram2.png
    :width: 650px
    :align: center