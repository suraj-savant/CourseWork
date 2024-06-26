import random

def k_means(data, k, max_iterations=1):
    # centroids = random.sample(data, k)
    centroids =[[1.0,1.0],[5.0,7.0]]
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return clusters, centroids  

def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        index = distances.index(min(distances))
        clusters[index].append(point)
    return clusters

def update_centroids(clusters):
    centroids = []
    for cluster in clusters:
        centroid = [sum(dim) / len(cluster) for dim in zip(*cluster)]
        centroids.append(centroid)
    return centroids

def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5



# Sample data
data = [
    [1,1], [1.5,2.0], [3,4],[5,7],[3.5,5],[4.5,5.0],[4.5,5.0],[3.5,4.5]
]

# Number of clusters
k = 2

# Running K-Means algorithm
clusters, centroids = k_means(data, k)

print("Final Clusters:", clusters)
print("Final Centroids:", centroids)
