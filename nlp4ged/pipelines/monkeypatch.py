from config import DATA_PATH, MODEL_PATH
from sklearn.pipeline import Pipeline 
from pathlib import Path
from sklearn.model_selection import KFold

import pandas as pd
from joblib import dump
import numpy as np

from nlp4ged.support.permutation_builder import PermutationBuilder
from nlp4ged.steps.normalizers import TextNormalizer
from nlp4ged.steps.vectorizers import TextVectorizer
from nlp4ged.steps.models import PredictiveModellers
from nlp4ged.dataclasses.corpus import Corpus
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report

"""
Monkey patch to check classification performance with smaller initial
tagged dataset.
"""



class Classifier:
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
    def __init__(self, params=classification_parameters, grid_search=False, data:Path=None):
            #TODO: What is going on in these 2 lines exactly?
        self.learning_data = data
        self.params=params
    
    def classify(self, use_model=False, existing_model=None, 
    blind_data:Path = None, save_model=False):
        # Use a pre-existing model.
        learning_corpus = Corpus(self.learning_data)
        X = learning_corpus['text']
        y = learning_corpus['tag']
        kfold = KFold(n_splits=7, shuffle=True, random_state=42)
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        for train_index, test_index in kfold.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            classification_pipeline = Pipeline(steps=[
                                ('normalizer', TextNormalizer(param_permutations=self.params)),
                                ("vectorizer", TextVectorizer(param_permutations=self.params)),
                                ("classifier", PredictiveModellers(param_permutations=self.params))]
                                )
        
            classification_pipeline.fit(X_train, y_train)
            y_pred = classification_pipeline.predict(X_test)
            accuracy_res = []
            accuracy = f1_score(y_test, y_pred, average='weighted')
            accuracy_res.append(accuracy)
            class_rep = classification_report(y_test, y_pred)
            print(class_rep)
        print("Accuracy:", np.mean(accuracy_res) )

if __name__ == "__main__":
    samples = ['sample_1_classified_1250.xlsx']
    for sample in samples:
        learning_data = DATA_PATH / 'input' / sample
        classifier = Classifier(data=learning_data)
        classifier.classify()


# data_full = DATA_PATH / 'input' / "complete_unclassified.xlsx"
# df = pd.read_excel(data_full, sheet_name=None)
# stats = []
# for key in df.keys():
#     print(len(df[key]))
#     stats.append(len(df[key]))



