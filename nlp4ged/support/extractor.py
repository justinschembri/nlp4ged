from sklearn.base import BaseEstimator, TransformerMixin
from config import DATA_PATH
import pandas as pd
import numpy as np
import os
from datetime import datetime
from sklearn.metrics import classification_report

"""
The DataExtractor Class is a dummy function performing the fit and transform 
methods such that it may be used with sklearn's pipeline Class. Input data is 
not modified. It prints out basic information about the transformed data from 
the previous pipeline step.
"""

class DataExtractor(BaseEstimator, TransformerMixin):

    def __init__(self, stage=None):
        self.stage = stage

    def fit (self, X, y=None):
        return self

    def transform(self, X):
        if self.stage == 'normalize':
            print('Size of split data: ' + str(X.shape[0]))
            return X
        if self.stage == 'vectorize':
            print('Number of features: ' + str(X.shape[1]))
            return X

#Function for extracting non-None parameters from the permutation parameters used in the pipeline:
def param_extractor(permutation_params):
            param_info = []
            for key in permutation_params.keys():
                if permutation_params[key] != None:
                    param_info.append(str(key)+ '=' +str(permutation_params[key]))
            return param_info

"""
The DataSaver class is used to write the outputs of intermediate fit_transform steps
Used in the pipeline. Its arguements are a dict containing permutation properties
defined in the pipeline. The merge method handles conversion of intermediate data
Outputs with varying dtypes.
"""

class DataSaver:

    # def __init__(self, permutation_params, step):
    #     self.permutation_params = permutation_params
    #     self.step = step
    #     self.date = datetime.today().strftime('%Y-%m-%d')
    #     self.path = '/Users/justin/Code/nlp4ged/_data/outputs/' + self.date + '-001/' + self.step + '/'
    #     self.suffix = int(self.path[52:55])
    #     if not os.path.exists(self.path):
    #         os.makedirs(self.path)
    #     else:
    #         latest = sorted(os.listdir(self.path))
    #         suffix = int(latest[-1][-2:])
    #         suffix = "-00" + (latest+1) + "/"
    #         self.path = '/Users/justin/Code/nlp4ged/_data/outputs/' + self.date + suffix + self.step + '/'
    #         os.makedirs(self.path)

    def __init__(self, permutation_params, step):
        self.permutation_params = permutation_params
        self.step = step
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.root = DATA_PATH / 'outputs'
        self.date_path = self.root + self.date + "-1/"
        self.path = self.date_path + self.step + "/"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        else:
            self.latest = sorted(os.listdir(self.root))
            latest = int(self.latest[-1][-1])
            if not os.path.exists(self.root + self.date + "-" + str(latest) + "/" + self.step + "/"):
                self.path = self.root + self.date + "-" + str(latest) + "/" + self.step + "/"
                os.makedirs(self.path)
            else:
                suffix = latest + 1
                self.path = self.root + self.date + "-" + str(suffix) + "/" + self.step + "/"
                os.makedirs(self.path)

    def merge(self, data):
        if isinstance(data, pd.Series):
            param_info = pd.Series(param_extractor(self.permutation_params))
            results = pd.concat([param_info, data])
            return results
        elif isinstance(data, np.ndarray):
            param_info = pd.Series(param_extractor(self.permutation_params))
            data = pd.Series(data)
            results = pd.concat([param_info, data])
            return results
        elif isinstance(data, pd.DataFrame):
            return data
    
    def extract(self, data):

        if isinstance(data, (pd.Series, np.ndarray)):
            results = self.merge(data)
            results.to_csv(self.path  + str(self.permutation_params['pref']) + '.csv', index=False, header=False)
        elif isinstance(data, pd.DataFrame):
            data.to_csv(self.path  + str(self.permutation_params['pref']) + '.csv', index=True, header=True)

def gen_report(y_test, y_pred):
    cr = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
    # Wrangle cr string output to a df format:
    cr = pd.DataFrame(cr).transpose()
    cr.loc['accuracy',('precision', 'recall', 'support')] = None
    cr.loc['accuracy', 'support'] = cr.loc['macro avg', 'support']
    return cr