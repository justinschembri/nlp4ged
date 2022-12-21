from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.base import BaseEstimator, TransformerMixin
from nlp4ged.support.extractor import DataSaver
import pandas as pd
import string

"""
A text normalization class applying multiple normalization techniques.
Normalization regime controlled by the class paramater 'type' declared upon iniatilization.
Expects text to be normalized as a pandas' series from an imported corpus.

There are three text normalizition regimes:
- basic - remove punctuation and lowercase only,
- medium - additionally removes stop words,
- high - additionally lemmitizes.
"""

class TextNormalizer(BaseEstimator, TransformerMixin):
    
    def __init__(self, param_permutations=None):
        self.param_permutations = param_permutations

    def fit (self, X, y=None):
        return self
                
    def basic_normalization(self, text):
        processed_text = []
        text = str(text)
        text = text.lower()
        for token in word_tokenize(text):
            if token in string.punctuation: continue
            processed_text.append(token)
        return processed_text
        
    def medium_normalization(self, text):
        processed_text = self.basic_normalization(text)
        for token in processed_text:
            if token in stopwords.words('english'):
                processed_text.remove(token)
        return processed_text

    def high_normalization(self, text):
        processed_text = self.medium_normalization(text)
        stemmer = SnowballStemmer('english')
        processed_text = [stemmer.stem(token) for token in processed_text]
        return processed_text

    def transform(self, documents):
        documents: pd.Series

        if self.param_permutations['ntype'] == 'basic':
            normalized_text = documents.apply(self.basic_normalization)
        elif self.param_permutations['ntype'] == 'medium':
            normalized_text = documents.apply(self.medium_normalization)
        elif self.param_permutations['ntype'] == 'high':
            normalized_text = documents.apply(self.high_normalization)
        # Saving text externally:
#        data_saver = DataSaver(self.param_permutations, 'normalize')
#        data_saver.extract(normalized_text)
        return normalized_text
