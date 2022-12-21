from nlp4ged.pipelines.classification import Classifier
from nlp4ged.pipelines.clustering_d2v import Clusterer
from nlp4ged.support.extractor import DataSaver
import matplotlib.pyplot as plt

import pandas as pd
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

clustering_parameters = {
                        'vtype':'doc2vec',
                        'd2v_size':128,
                        'd2v_alpha':0.025,
                        'd2v_epoch':30,
                        'mtype':'svc',
                        'svc_dual':True,
                        'ntype':'high',
                        'drange':[['all']],
                        'pref':'selected'}

def classify(save=True, persist=False):
    print("Parameters predetermined, loading ...")
    #TODO: Allow a new grid-search to be carried out.
    classifier = Classifier(params=classification_parameters, grid_search=False)
    if persist==True:
        classified_data = classifier.classify(save_model=True)
    elif persist==False:
        classified_data = classifier.classify(save_model=False)
    if save == True:
        data_saver = DataSaver(classification_parameters, action)
        data_saver.extract(classified_data)
        print(classified_data)
        print("Classified data saved to disk.")
    elif save == False:
        return classified_data

def cluster(save=True):
    print("Clustering and classification parameters predetermined, loading ...")
    classified_data = classify(save=False)
    clusterer = Clusterer(classified_data=classified_data,
                            params=clustering_parameters)
    clustered_data = clusterer.cluster()
    print(clustered_data)
    if save == True:
        data_saver = DataSaver(clustering_parameters, action)
        data_saver.extract(clustered_data)
        print("Clustered data saved to disk.")

def cluster_inspect(save=False):
    classified_data = classify(save=False)
    clusterer = Clusterer(classified_data=classified_data,
                            params=clustering_parameters)
    K_range, squared_distances_sum = clusterer.cluster(k_inspect=True)
    plt.plot(K_range, squared_distances_sum, '-bx')
    plt.xlabel('k')
    plt.ylabel('Sum of Squared Distances')
    plt.title('Elbow Method for Optimal K')
    plt.show()

if __name__ == "__main__":

    print("Select action: [classify] [cluster]:")
    function_map = {"classify":classify,
                    "classify-save":classify,
                     "cluster":cluster, 
                     "cluster-inspect":cluster_inspect}
    action = input()
    
    if action == 'classify':
        print("Save model for later use? y/n")
        query = input()
        if query == "y":
            action = "classify-save"
            function_map[action](persist=True)
        if query == "n":
            action = "classify"
            function_map[action]()

    if action == "cluster":
        print("Inspect K-Clustering? y/n")
        query = input()
        if query == 'y':
            action = "cluster-inspect"
            function_map[action]()
        if query == 'n':
            action = 'cluster'
            function_map[action]()