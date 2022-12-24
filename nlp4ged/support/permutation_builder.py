"""
The PermutationBuilder class constructs are structured list of dicts containing a set of hyperparameters
to be used with the clustering pipeline. The set of hyperparameters is explicitly stated in the
__init__ of the class. 
"""
class PermutationBuilder:

    def __init__(self):
        # Set up range of normalizer, vectorizer or model params:
        self.date_range_gaps = [3, 9]
        self.normalizer_model_types = ['basic', 'medium', 'high']
        self.vectorizer_model_types = ['doc2vec', 'tfidf']
        self.predictive_model_types = ['svc', 'randomforest'] # Naive Bayes disabled.

        # Set up individual vectorizer model params:
        # TFIDF:
        self.vectorizer_tfidf_max_features = [128, 256]
        self.vectorizer_tfidf_ngram_ranges = [(1,1), (2,3),(3,7)]
        # Doc2Vec:
        self.vectorizer_d2v_size = [128, 256]
        self.vectorizer_d2v_alpha = [0.025, 0.1]
        self.vectorizer_d2v_epoch = [10, 30]
        
        # Set up individual predictive model params:
        # RandomForest:
        self.rf_max_depth = [10, 50, 100]
        self.rf_samples_split = [3, 10]
        self.rf_samples_leaf = [1, 3]
        self.rf_bootstrap = [True, False]
        # LinearSVC:
        self.svc_dual = [True, False]
        # MultinomialNB:
        self.nb_alpha = [0.00001, 0.001, 0.1, 1, 10, 100, 1000]

    def date_perms(self):
        
        date_range = range(5,23)
        ranges = []
        for gap in self.date_range_gaps:
            for count, date in enumerate(date_range):
                if count == 0:
                    start_date = date
                    end_date = date + (gap-1)
                    ranges.append([start_date, end_date])
                else:
                    start_date = end_date
                    end_date = start_date + (gap-1)
                    if end_date >= max(date_range):
                        break
                    else:
                        ranges.append([start_date, end_date])
            if max(max(ranges)) != max(date_range):
                last_date = [max(max(ranges)), max(date_range)]
                ranges.append(last_date)
        
        ranges.append(['all'])
        return ranges

    def vectorizer_perms(self):

        vectorizer_permutations = []

        for vectorizer_model in self.vectorizer_model_types:
            # There should be as many if loops as there are models.
            if vectorizer_model == 'tfidf':
                # There should be as many for loops as there are model-specific parameters.
                for max_feature in self.vectorizer_tfidf_max_features:
                    for ngram_range in self.vectorizer_tfidf_ngram_ranges:
                        permutation = {'vtype':vectorizer_model, 'max_features':max_feature, 'ngram_range':ngram_range}
                        vectorizer_permutations.append(permutation)
            
            elif vectorizer_model == 'doc2vec':
                for size in self.vectorizer_d2v_size:
                    for alpha in self.vectorizer_d2v_alpha:
                        for epoch in self.vectorizer_d2v_epoch:
                            permutation = {'vtype':vectorizer_model, 'd2v_size':size, 'd2v_alpha':alpha, 'd2v_epoch':epoch}
                            vectorizer_permutations.append(permutation)
    
        return vectorizer_permutations

    def model_perms(self):

        model_permutations = []

        for model in self.predictive_model_types:
            # There should be as many if loops as there are models.
            if model == 'randomforest':
                # There should be as many for loops as there are model-specific parameters.
                for max_depth in self.rf_max_depth:
                    for sample_split in self.rf_samples_split:
                        for sample_leaf in self.rf_samples_leaf:
                            for bootstrap in self.rf_bootstrap:
                                permutation = {'mtype':model, 'rf_max_depth':max_depth, 
                                                'rf_samples_split':sample_split,
                                                'rf_samples_leaf':sample_leaf,
                                                'rf_bootstrap':bootstrap}
                                model_permutations.append(permutation)

            elif model == 'svc':
                for svc_dual in self.svc_dual:
                    permutation = {'mtype':model, 'svc_dual':svc_dual}
                    model_permutations.append(permutation)
            
            elif model == 'naivebayes':
                for nb_alpha in self.nb_alpha:
                    permutation = {'mtype':model, 'nb_alpha':nb_alpha}
                    model_permutations.append(permutation)

        return model_permutations

    def build(self) -> dict:
        built_permutation = []
        pref = 0
        for normalizer_model in self.normalizer_model_types:
            for vectorizer_permutation in self.vectorizer_perms():
                for model_permutation in self.model_perms():
                    for drange in self.date_perms():
                        permutation = vectorizer_permutation | model_permutation | {'ntype':normalizer_model} | {'pref': pref} | {'drange':drange}
                        built_permutation.append(permutation)
                        pref += 1
        
        return built_permutation