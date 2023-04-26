import numpy as np
import random
import math


class Kmeans:
    def __init__(self, X, K, max_iters):
        # Data
        self.X = X
        # Number of clusters
        self.K = K
        # Number of maximum iterations
        self.max_iters = max_iters
        # Initialize centroids
        self.centroids = self.init_centroids()

    def init_centroids(self):
        """
        Selects k random rows from inputs and returns them as the chosen centroids.
        You should randomly choose these rows without replacement and only
        choose from the unique rows in the dataset. Hint: look at
        Python's random.sample function as well as np.unique
        :return: a Numpy array of k cluster centroids, one per row
        """
        # TODO
        unique_rows = np.unique(self.X, axis=0)
        return np.array(random.sample(list(unique_rows), self.K))

    def euclidean_dist(self, x, y):
        """
        Computes the Euclidean distance between two points, x and y

        :param x: the first data point, a Python numpy array
        :param y: the second data point, a Python numpy array
        :return: the Euclidean distance between x and y
        """
        # TODO
        return np.linalg.norm(x-y)

    def closest_centroids(self):
        """
        Computes the closest centroid for each data point in X, returning
        an array of centroid indices
 
        :return: an array of centroid indices
        """
        # TODO
        centroid_indices = []
        for i in range(self.X.shape[0]):
            distances = np.array([self.euclidean_dist(self.X[i], j) for j in self.centroids])
            closest_centroid_ind = np.argmin(distances)
            centroid_indices.append(closest_centroid_ind)

        return np.array(centroid_indices)        
        

        # uses euclidean distance
        #  To determine the centroids’ new locations, you average together the data points for
        #  which that was the closest centroid
        

    def compute_centroids(self, centroid_indices):
        """
        Computes the centroids for each cluster, or the average of all data points
        in the cluster. Update self.centroids.

        Check for convergence (new centroid coordinates match those of existing
        centroids) and return a Boolean whether k-means has converged

        :param centroid_indices: a Numpy array of centroid indices, one for each datapoint in X
        :return boolean: whether k-means has converged
        """
        # TODO
        new_centroids = []
        for i in range(self.K): # for each cluster, 
            cluster_data = self.X[centroid_indices == i] #all data points for that centroid
            new_centroid = np.mean(cluster_data, axis=0) # average them all to find new centroid
            new_centroids.append(new_centroid) # adding to new list
        new_centroids = np.array(new_centroids)
        converged = np.allclose(self.centroids, new_centroids)
        
        if not converged:
            self.centroids = new_centroids

        return converged


    def run(self):
        """
        Run the k-means algorithm on dataset X with K clusters for max_iters.
        Make sure to call closest_centroids and compute_centroids! Stop early
        if algorithm has converged.
        :return: a tuple of (cluster centroids, indices for each data point)
        Note: cluster centroids and indices should both be numpy ndarrays
        """
        # TODO
        for i in range(self.max_iters):
            centroid_array = self.closest_centroids()
            if self.compute_centroids(centroid_array):
                break
         
        return (self.centroids, centroid_array)
    

    def inertia(self, centroids, centroid_indices):
        """
        Returns the inertia of the clustering. Inertia is defined as the
        sum of the squared distances between each data point and the centroid of
        its assigned cluster.

        :param centroids - the coordinates that represent the center of the clusters
        :param centroid_indices - the index of the centroid that corresponding data point it closest to
        :return inertia as a float
        """
        # TODO
    
        squared_distances = np.sum((self.X - centroids[centroid_indices])**2)
        return float(np.sum(squared_distances))
    
