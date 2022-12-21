from nlp4ged.support.extractor import DataSaver, gen_report
from sklearn.pipeline import Pipeline 
from typing import Dict
import pandas as pd
from joblib import dump

from nlp4ged.support.permutation_builder import PermutationBuilder
from nlp4ged.steps.normalizers import TextNormalizer
from nlp4ged.steps.vectorizers import TextVectorizer
from nlp4ged.steps.models import PredictiveModellers
from nlp4ged.support.corpus_importer import CorpusImporter

"""
Classification pipeline. Will itterate across a range of hyperparamters, explicility set in the
permutationBuilder class. For each itteration, outputs of the intermediate steps (normalization and 
vectorization) and the classification reports will be saved to the root folder ~/data/output. The 
index of the itteration with best overall performance will be printed.
"""
class Classifier:
    def __init__(self, params, grid_search=False, use_model=False):
        if use_model == False:
            self.learning_data = '/Users/justin/Code/nlp4ged/_data/_learning/learning.xlsx'
            self.blind_data = '/Users/justin/Code/nlp4ged/_data/_blind/blind.xlsx'
            if grid_search == True:
                permutation_builder = PermutationBuilder()
                generated_permutations = permutation_builder.build()
                self.params = generated_permutations
                self.total_params = len(generated_permutations)
                self.accuracy_dict = {}
                self.count = 0
            else:
                self.params = params
        elif use_model == True:
            pass
    
    def classify(self, use_model=False, existing_model=None, blind_data=None, save_model=False):
        if use_model == True:
            blind_corpus = CorpusImporter(blind_data)
            X_blind = blind_corpus.text
            cfref = blind_corpus.ref
            classification_pipeline = existing_model

        elif use_model == False:
            learning_corpus = CorpusImporter(self.learning_data)
            X_train = learning_corpus.text
            y_train = learning_corpus.tag
            cfref = learning_corpus.ref
            blind_corpus = CorpusImporter(self.blind_data)
            X_blind = blind_corpus.text

            classification_pipeline = Pipeline(steps=[
                                ('normalizer', TextNormalizer(param_permutations=self.params)),
                                ("vectorizer", TextVectorizer(param_permutations=self.params)),
                                ("classifier", PredictiveModellers(param_permutations=self.params))]
                                )

            classification_pipeline.fit(X_train, y_train)
            if save_model == True:
                    dump(classification_pipeline, 'classifier_model.joblib')

        y_pred = classification_pipeline.predict(X_blind)
        y_pred = pd.DataFrame(y_pred)
        X_blind_tagged = pd.DataFrame(X_blind)
        X_blind_tagged['PREDICTION'] = y_pred
        X_blind_tagged['CFREF'] = cfref
        X_blind_noiseless = X_blind_tagged[X_blind_tagged['PREDICTION'] != 0]

        return X_blind_noiseless

