# dendrogram-timeseries
Scipy's dendrogram for agglomerative clustering requires extensive customizations
to make it more informative. This package wraps scipy's dendrogram with two customizations:
 * Timeseries graph at the side
 * Distance labels and cluster split points
 

## Installation
Download ``dendrogram_ts.py`` and put in your python site-package or project folder.

## Plot by Maximum Clusters
```python
from dendrogram_ts import maxclust_draw

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(8,5));

maxclust_draw(df, 'ward', 'euclidean', max_cluster=10, ts_hspace=2)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram1.png" width="600">

## Plot by Color Threshold

```python
from dendrogram_ts import colorclust_draw
import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 1
plt.style.use('seaborn-white')
plt.figure(figsize=(12,10))

colorclust_draw(df, method='ward', metric='euclidean', color_threshold=5200, ts_hspace=1)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram3.png" width="650">

## Plot All Clusters

```python
from dendrogram_ts import allclust_draw

plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))

allclust_draw(df, 'ward', 'euclidean', ts_hspace=5)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram2.png" width="600">
