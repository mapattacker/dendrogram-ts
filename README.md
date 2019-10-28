# dendrogram-timeseries
Scipy dendrogram for agglomerative clustering is good, but requires extensive customizations
to make it more informative.

This package wraps scipy's dendrogram with two customizations:
 * Distance labels and cluster split points
 * Timeseries graph at the side

## Installation
Download ``dendrogram_ts.py`` and put in your site-package folder.

## Plot by MaxClusters
```python
from dendrogram_ts import maxclust_draw

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8,5));
maxclust_draw(df.T, 'ward', 'euclidean', 8, 1)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram1.png" width="600">

## Pipeline
1. Timeseries graph for all clusters
2. Timeseries graph by color threshold
3. Compile package to pip 
