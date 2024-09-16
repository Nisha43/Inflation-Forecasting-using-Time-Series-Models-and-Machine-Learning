from sklearn.cluster import KMeans

def kmeans_clustering(X, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    return kmeans
