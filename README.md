# dendrogram-timeseries
Scipy dendrogram for agglomerative clustering is good, but requires extensive customizations
to make it more informative.

This package adds two customizations:
 * Distance labels and cluster split points
 * Timeseries graph at the side


```python
from dendrogram_ts import maxclust_draw

plt.figure(figsize=(8,5));
maxclust_draw(df.T, 'ward', 'euclidean', 8, 1)
```

<img src="https://github.com/mapattacker/dendrogram-timeseries/blob/master/images/dendrogram1.png" width="600">

### Pipeline
1. Timeseries graph for all clusters
2. Timeseries graph by color threshold
