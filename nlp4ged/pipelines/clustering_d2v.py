from nlp4ged.steps.normalizers import TextNormalizer
from nlp4ged.steps.vectorizers import TextVectorizer
from sklearn.cluster import KMeans
from nlp4ged.support.text_processing import lower_case

import pandas as pd

"""
Clustering pipeline. Repeats the classification procedure with a set of explicility declared
Hyper parameters (these should be based on the results of the classification pipeline).
Clustering parameters are also explicitly declared. Script will also produce a plot which can
Be interpreted by the 'elbow method'. Cluster sizes are explictly declared by the variable
n_clusters. Cluster text will be saved to ~/data/output and word clouds will be generated.
"""
# Repeat the classification pipeline and test on blind data:
# classification_parameters = {
#                         'vtype':'tfidf',
#                         'max_features':256,
#                         'ngram_range':(1,1),
#                         'mtype':'svc',
#                         'svc_dual':True,
#                         'ntype':'basic',
#                         'drange':[['all']],
#                         'pref':'selected'}

# training_corpus = CorpusImporter('data/1.xlsx')
# X_train = training_corpus.text
# y_train = training_corpus.tag

# blind_corpus = CorpusImporter('data/3.xlsx')
# X_blind = blind_corpus.text

# classification_pipeline = Pipeline(steps=[
#                     ('normalizer', TextNormalizer(param_permutations=classification_parameters)),
#                     ("vectorizer", TextVectorizer(param_permutations=classification_parameters)),
#                     ("classifier", PredictiveModellers(param_permutations=classification_parameters))]
#                     )

# classification_pipeline.fit(X_train, y_train)
# y_pred = classification_pipeline.predict(X_blind)
# y_pred = pd.DataFrame(y_pred)
# X_blind_tagged = pd.DataFrame(X_blind)
# X_blind_tagged['PREDICTION'] = y_pred
# X_blind_noiseless = X_blind_tagged[X_blind_tagged['PREDICTION'] != 0]

# Clustering pipeline on remaining data:

class Clusterer():
    def __init__(self, classified_data, params):
        self.classified_data = classified_data
        self.text = classified_data['TEXT']
        self.params = params


# self.text = X_blind_noiseless['TEXT']
    def cluster(self, k_inspect=False):
        normalizer = TextNormalizer(param_permutations=self.params)
        X_normalized = normalizer.fit_transform(self.text)
        vectorizer = TextVectorizer(param_permutations=self.params)
        d2v_model, X_vectorized = vectorizer.doc2vec(X_normalized)
        X_vectorized = [d2v_model.infer_vector(x) for x in X_normalized]


# 45 clusters appear ideal. 
        n_clusters = 22
        cluster_model = KMeans(n_clusters=n_clusters)
        X_clusters = cluster_model.fit_predict(X_vectorized)
        X_clustered = pd.DataFrame(self.text)
        X_clustered['CLUSTER'] = X_clusters
        X_clustered = X_clustered.sort_values('CLUSTER')
        X_clustered_lower = X_clustered.applymap(lower_case())
        if k_inspect == False:
            return X_clustered_lower
        elif k_inspect==True:
            K_range = range(1, 75)
            squared_distances_sum = []
            for K in K_range:
                clustering_model = KMeans(n_clusters=K)
                clustering_model.fit(X_vectorized)
                squared_distances_sum.append(clustering_model.inertia_)
            return K_range, squared_distances_sum



# data_saver = DataSaver(classification_parameters, 'cluster')
# data_saver.extract(X_clustered)

# Draw wordclouds.
# cluster_range = range(n_clusters)
# for cluster in cluster_range:
#     text = X_clustered[X_clustered['cluster'] == cluster]
#     text = str(text.values)
#     wordcloud = WordCloud().generate(text)
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.show()
