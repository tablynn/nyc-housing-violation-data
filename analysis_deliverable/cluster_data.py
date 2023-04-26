
import matplotlib.pyplot as plt
from matplotlib import cm
from kmeans import Kmeans
import pandas as pd
import numpy as np

feature_columns = ["latitude", "longitude", "med_income"]
MAX_CLUSTERS = 10
cmap = cm.get_cmap('tab10', MAX_CLUSTERS)

def visualize_violation_clusters(data, centroids=None, centroid_indices=None,
                             is_lib_kmean=False):
    """
    Visualizes the song data points and (optionally) the calculated k-means
    cluster centers.
    Points with the same color are considered to be in the same cluster.

    Optionally providing centroid locations and centroid indices will color the
    data points to match their respective cluster and plot the given centroids.
    Otherwise, only the raw data points will be plotted.

    :param data: 2D numpy array of song data
    :param centroids: 2D numpy array of centroid locations
    :param centroid_indices: 1D numpy array of centroid indices for each data point in data
    :return:
    """
    def plot_songs(fig, color_map=None):
        x, y, z = np.hsplit(data, 3)
        fig.scatter(x, y, z, c=color_map)

    def plot_clusters(fig):
        x, y, z = np.hsplit(centroids, 3)
        fig.scatter(x, y, z, c="black", marker="x", alpha=1, s=200)

    plt.clf()
    cluster_plot = centroids is not None and centroid_indices is not None

    ax = plt.figure(num=1).add_subplot(111, projection='3d')
    colors_s = None

    if cluster_plot:
        if max(centroid_indices) + 1 > MAX_CLUSTERS:
            print(f"Error: Too many clusters. Please limit to fewer than {MAX_CLUSTERS}.")
            exit(1)
        colors_s = [cmap(l / MAX_CLUSTERS) for l in centroid_indices]
        plot_clusters(ax)

    plot_songs(ax, colors_s)

    ax.set_xlabel(feature_columns[0])
    ax.set_ylabel(feature_columns[1])
    ax.set_zlabel(feature_columns[2])

    plot_name = "/data"
    plot_name = plot_name + "_clusters" if cluster_plot else plot_name + "_raw"
    plot_name = plot_name + "_sklearn" if is_lib_kmean else plot_name

    ax.set_title(plot_name[1:])
    
    # Helps visualize clusters
    plt.gca().invert_xaxis()
   # plt.savefig(output_dir + plot_name + ".png")
    plt.show()

def read_data(path):
    # df = pd.read_csv('data/housing_income_merged.csv') 
    # df = df[['latitude', 'longitude', 'year_of_violation', 'med_income']]
    # print(df)
    with open(path) as data_file:
        data = pd.read_csv(data_file)[feature_columns].to_numpy()
    print(data)
    return data    
    

def clustering(data, max_iters):
    k = 4
    centroids, idx = Kmeans(data, k, max_iters).run()

    visualize_violation_clusters(data, centroids=centroids, centroid_indices=idx,
                             is_lib_kmean=False)
    return centroids, idx

def main():
    """
    Main function for running song clustering. You should not have to change
    anything in this function.
    """
    # Set random seeds
    #np.random.seed(0)
    #random.seed(0)

   # data, music_data = read_data(data_dir)
    #max_iters = 300  # Number of times the k-mean should run

    #if not os.path.exists(output_dir):
     #   os.makedirs(output_dir)
    path = '../data_deliverable/data/housing_income_merged.csv'

    data = read_data(path)

    max_iters = 300
    centroids, idx = clustering(data, max_iters=max_iters)
   # export_centroid_idx(centroids, idx, centroids_sklearn, idx_sklearn)


if __name__ == '__main__':
    # Make args global variable
    #args = parse_args()
    
   # data_dir = args.d
   # output_dir = args.o

    main()
