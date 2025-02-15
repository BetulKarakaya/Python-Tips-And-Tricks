import numpy as np
import matplotlib.pyplot as plt

class SimpleKMeans:
    
    def __init__(self, k, max_iters=100, tol=1e-4):
        """ Initialize K-Means clustering with k clusters, max iterations, and convergence tolerance. """
        self.k = k
        self.max_iters = max_iters
        self.tol = tol  # Convergence threshold
        self.centroids = None  # Cluster centers

    def fit(self, X):
        """ Fit K-Means clustering on the given dataset. """
        self.X = np.array(X)
        n_samples, n_features = self.X.shape
        
        # Randomly initialize k centroids
        random_indices = np.random.choice(n_samples, self.k, replace=False)
        self.centroids = self.X[random_indices]

        for _ in range(self.max_iters):
            # Assign each point to the closest centroid
            distances = np.linalg.norm(self.X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)

            # Compute new centroids as the mean of assigned points
            new_centroids = np.array([self.X[labels == i].mean(axis=0) for i in range(self.k)])

            # Check for convergence (if centroids do not change significantly)
            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                break

            self.centroids = new_centroids  # Update centroids

        self.labels = labels  # Store final labels

    def predict(self, X_new):
        """ Predict the cluster for new data points. """
        distances = np.linalg.norm(X_new[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def visualize(self):
        """ Visualize the clustered data points and centroids (for 2D data). """
        if self.X.shape[1] != 2:
            print("Visualization is only available for 2D data.")
            return

        plt.scatter(self.X[:, 0], self.X[:, 1], c=self.labels, cmap='viridis', alpha=0.6, edgecolors='k')
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], c='red', marker='X', s=200, label="Centroids")
        
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.title(f"K-Means Clustering with k={self.k}")
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    np.random.seed(42)
    
    # Generate some artificial 2D data (3 clusters)
    cluster_1 = np.random.normal(loc=[5, 5], scale=1.5, size=(50, 2))
    cluster_2 = np.random.normal(loc=[15, 15], scale=1.5, size=(50, 2))
    cluster_3 = np.random.normal(loc=[25, 5], scale=1.5, size=(50, 2))
    
    data = np.vstack((cluster_1, cluster_2, cluster_3))  # Combine clusters into one dataset
    
    # Apply K-Means clustering
    kmeans = SimpleKMeans(k=3)
    kmeans.fit(data)
    kmeans.visualize()

    # Predict new points
    new_points = np.array([[10, 10], [20, 3], [6, 5]])
    predicted_clusters = kmeans.predict(new_points)
    print(f"Predicted clusters for new points {new_points}: {predicted_clusters}")


if __name__ == "__main__":
    main()
