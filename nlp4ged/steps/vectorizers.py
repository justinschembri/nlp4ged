from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from nlp4ged.support.extractor import DataSaver
import numpy as np

"""
Several vectorizer functions. 
Expects pre-processed text as a pandas' series from text_normalizers.
"""

def dummy_func(text):
    return text

class TextVectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, param_permutations=None):

        self.param_permutations = param_permutations
        #where the vectorizer and its params are initiated:
        if self.param_permutations['vtype'] == 'tfidf':
            max_features=self.param_permutations['max_features']
            ngram_range=self.param_permutations['ngram_range']
            
            self.tfidf = TfidfVectorizer(
                tokenizer=dummy_func,
                preprocessor=dummy_func,
                token_pattern=None,
                max_features=max_features,
                ngram_range=ngram_range)
        
        elif self.param_permutations['vtype'] == 'doc2vec':
            self.d2v_size=self.param_permutations['d2v_size']
            self.d2v_alpha=self.param_permutations['d2v_alpha']
            self.d2v_epoch=self.param_permutations['d2v_epoch']

    def fit(self, X, y=None):
        if self.param_permutations['vtype'] == 'tfidf':
            fit_model = self.tfidf.fit(X)
            return fit_model

    def transform(self, X):
        if self.param_permutations['vtype'] == 'tfidf':
            transformed_model = self.tfidf.transform(X)
            feature_names = self.tfidf.get_feature_names_out()
            # data_saver = DataSaver(self.param_permutations, 'vectorize')
            # data_saver.extract(feature_names)
            return transformed_model
    
    def doc2vec(self, X):
            X_train = [TaggedDocument(words, ['d{}'.format(idx)]) for idx, words in enumerate(X)]
            d2v_model = Doc2Vec(X_train, vector_size=self.d2v_size, alpha=self.d2v_alpha, epochs=self.d2v_epoch)
            X_train = [d2v_model.dv[x] for x in range(len(X))]
            # data_saver = DataSaver(self.param_permutations, 'vectorize')
            # blank_array = np.array([])
            # data_saver.extract(blank_array)
            return d2v_model, X_train


