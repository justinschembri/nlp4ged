from nlp4ged.pipelines.classification import Classifier
from nlp4ged.pipelines.clustering_d2v import Clusterer
from nlp4ged.support.permutation_builder import PermutationBuilder
from nlp4ged.support.extractor import DataSaver
from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt

# Classification and clustering parameters are currently fixed.
classification_parameters = {
                        'vtype':'tfidf',
                        'max_features':256,
                        'ngram_range':(1,1),
                        'mtype':'svc',
                        'svc_dual':True,
                        'ntype':'basic',
                        'drange':[['all']],
                        'pref':'results'
                            }

# clustering_parameters_d2v = {
#                         'vtype':'doc2vec',
#                         'd2v_size':128,
#                         'd2v_alpha':0.025,
#                         'd2v_epoch':30,
#                         'mtype':'svc',
#                         'svc_dual':True,
#                         'ntype':'high',
#                         'drange':[['all']],
#                         'pref':'selected'}

permutation_builder = PermutationBuilder()
permutations = permutation_builder.build()

def classify(save=False, persist=False):
    print("Parameters predetermined, loading ...")
    #TODO: Allow a new grid-search to be carried out.
    classifier = Classifier(params=classification_parameters, grid_search=False)
    if persist==True:
        classified_data = classifier.classify(save_model=True)
    elif persist==False:
        classified_data = classifier.classify(save_model=False)
    # if save == True:
    #     data_saver = DataSaver(classification_parameters, action)
    #     data_saver.extract(classified_data)
    #     print(classified_data)
    #     print("Classified data saved to disk.")
    if save == False:
        return classified_data

def cluster():
    print("Clustering and classification parameters predetermined, loading ...")
    silhouette_scores = []
    k_numbers = []
    classified_data = classify(save=False)
    cluster_range = [10,20,30]
    for permutation in permutations:
        for k in cluster_range:
            if permutation["pref"] != 312:
                pass
            else:
                clusterer = Clusterer(classified_data=classified_data,
                                        params=permutation)
                X, labels = clusterer.cluster(return_X=True, n_clusters=22)
                # silhouette_avg = silhouette_score(X, labels)
                # # print(silhouette_avg)
                # silhouette_scores.append(silhouette_avg)
                # k_numbers.append(k)
                # print(silhouette_avg)
                return X, labels

## Dimensionality Reduction and Plot
# X_clusters = labels
# X_vectorized = X

# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA

# # Assuming X_clusters is a list/array containing the cluster labels
# # and X_vectorized is a list/array containing the vectorized data points

# # Apply PCA for dimensionality reduction
# pca = PCA(n_components=2)
# reduced_vectors = pca.fit_transform(X_vectorized)

# # Create a list of unique cluster labels
# unique_labels = list(set(X_clusters))

# # Assign colors to each cluster label
# colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink',
#                    'gray', 'olive', 'cyan', 'gold', 'lime', 'teal', 'indigo',
#                    'violet', 'magenta', 'salmon', 'yellow', 'tan', 'lavender',
#                    'turquoise', 'lightgreen']  # You can add more colors if needed
# plt.figure(figsize=(10, 10))
# # Create a scatter plot for each data point, colored by the cluster labels
# for label, color in zip(unique_labels, colors):
#     # Filter the data points belonging to the current cluster label
#     clustered_points = [reduced_vectors[i] for i in range(len(X_clusters)) if X_clusters[i] == label]
#     # Plot the clustered points with the assigned color
#     plt.scatter(*zip(*clustered_points), color=color, label=f'Cluster {label}')

# # Add labels and legend
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.legend(loc='upper right')

# plt.savefig('cluster_plot.png', dpi=300)
# # Show the plot
# plt.show()

# # Show the plot
# plt.show()
    # if save == True:
    #     data_saver = DataSaver(clustering_parameters, action)
    #     data_saver.extract(clustered_data)
    #     print("Clustered data saved to disk.")

# def cluster_inspect(save=False):
#     classified_data = classify(save=False)
#     clusterer = Clusterer(classified_data=classified_data,
#                             params=clustering_parameters)
#     K_range, squared_distances_sum = clusterer.cluster(k_inspect=True)
#     plt.plot(K_range, squared_distances_sum, '-bx')
#     plt.xlabel('k')
#     plt.ylabel('Sum of Squared Distances')
#     plt.title('Elbow Method for Optimal K')
#     plt.show()