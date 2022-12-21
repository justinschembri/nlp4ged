import pandas as pd
import os, sys, pathlib
from joblib import load
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
from nlp4ged.analysis.contamination import calculate_contamination
from nlp4ged.support.text_processing import lower_case, remove_punctuation
from nlp4ged.logic.conclusion_populater import populate_conclusions
from nlp4ged.pipelines.classification import Classifier

def process_data(data='selected'):
    # Point to dataset.
    rootFolder = os.path.dirname(os.path.dirname(
        str(pathlib.Path(sys.argv[0]).resolve())))
    if data == 'blind':
        # folder = rootFolder + '/_data/_blind'
        folder = '~/Code/nlp4ged/_data/_blind'
        file = '/all.xlsx'
        path = folder + file

    elif data == 'selected':
        # folder = rootFolder + '/_data/_selected'
        folder = '~/Code/nlp4ged/_data/_selected'
        file = '/selected.csv'
        path = folder + file

    # Load classifier model, classify, dump noise.
    existing_classifier = load('/Users/justin/Code/nlp4ged/classifier_model.joblib')
    classifier = Classifier(params=None, grid_search=False, use_model=True)
    noiseless_data = classifier.classify(use_model=True, 
                        existing_model=existing_classifier, 
                        blind_data=path)

    # Generate a match matrix, some preprocessing.
    noiseless_data = noiseless_data.applymap(lower_case())
    noiseless_data['TEXT'] = noiseless_data['TEXT'].apply(remove_punctuation)
    regex_list = regex_importer()
    match_matrix = match_matricizer(noiseless_data, regex_list)
    # Store contamination matrix.
    #contamination_matrix = calculate_contamination(match_matrix, regex_list)
    # Run logic on matches, populate GED attributes columns.
    conclusion_matrix = populate_conclusions(match_matrix)
    return conclusion_matrix

if __name__ == "__main__":
    conclusion_matrix = process_data(data='blind')
    conclusion_matrix['CFREF'] = conclusion_matrix['CFREF'].str.upper()
    conclusion_matrix.to_csv('~/Code/nlp4ged/_data/outputs/all.csv')
    print(conclusion_matrix)
