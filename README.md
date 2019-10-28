# dendrogram-timeseries
Scipy dendrogram for agglomerative clustering is good, but requires extensive customizations
to make it more informative.

This package wraps scipy's dendrogram with two customizations:
 * Distance labels and cluster split points
 * Timeseries graph at the side

## Installation
Download ``dendrogram_ts.py`` and put in your python site-package or project folder.

## Plot by Maximum Clusters
```python
from dendrogram_ts import maxclust_draw

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8,5));
maxclust_draw(df.T, 'ward', 'euclidean', max_cluster=10, ts_space=2)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram1.png" width="600">

## Plot All Clusters

```python
from dendrogram_ts import maxclust_draw

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
allclust_draw(df.T, 'ward', 'euclidean', ts_space=5)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram2.png" width="600">

## Pipeline
1. Timeseries graph by color threshold
2. Compile package to pip 
