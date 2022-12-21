from sklearn.naive_bayes import MultinomialNB
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

"""
Predictive models. Paramaters are set by the kwarg 'param_permutations' which is generated
by the PermutationBuilder class. Currently supports Random Forest and LinearSVC.
"""

class PredictiveModellers(BaseEstimator, TransformerMixin):

    def __init__(self, param_permutations=None):

        self.param_permutations = param_permutations

        if self.param_permutations['mtype'] == 'randomforest':
            self.rf_max_depth = param_permutations['rf_max_depth']
            self.rf_samples_split = param_permutations['rf_samples_split']
            self.rf_samples_leaf = param_permutations['rf_samples_leaf']
            self.rf_bootstrap = param_permutations['rf_bootstrap']

            self.randomforest = RandomForestClassifier(max_depth=self.rf_max_depth,
                                                        min_samples_split=self.rf_samples_split,
                                                        min_samples_leaf=self.rf_samples_leaf,
                                                        bootstrap=self.rf_bootstrap
                                                        )
        elif self.param_permutations['mtype'] == 'svc':
            self.svc_dual = param_permutations['svc_dual']
            
            self.svc = LinearSVC(dual=self.svc_dual)
        elif self.param_permutations['mtype'] == 'naivebayes':
            self.nb_alpha = param_permutations['nb_alpha']

            self.nb = MultinomialNB(alpha=self.nb_alpha)

    def fit(self, X, y=None):
        if self.param_permutations['mtype'] == 'randomforest':
            fit_model = self.randomforest.fit(X,y)
        elif self.param_permutations['mtype'] == 'svc':
            fit_model = self.svc.fit(X,y)
        elif self.param_permutations['mtype'] == 'naivebayes':
            fit_model = self.nb.fit(X,y)
    
    def predict(self, X):
        if self.param_permutations['mtype'] == 'randomforest':
            prediction = self.randomforest.predict(X)
            return prediction
        elif self.param_permutations['mtype'] == 'svc':
            prediction = self.svc.predict(X)
            return prediction
        elif self.param_permutations['mtype'] == 'naivebayes':
            prediction = self.nb.predict(X)
            return prediction
