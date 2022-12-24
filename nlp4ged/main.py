from config import DATA_PATH, MODEL_PATH
from joblib import load
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
from nlp4ged.support.text_processing import lower_case, remove_punctuation
from nlp4ged.logic.conclusion_populater import populate_conclusions
from nlp4ged.pipelines.classification import Classifier

def process_data(data='selected'):
    # A wrapper to process the blind dataset using a pre-trained model.

    if data == 'blind':
        path = DATA_PATH / '_blind' / 'all.xlsx'

    elif data == 'selected':
        # folder = rootFolder + '/_data/_selected'
        path = DATA_PATH / '_selected' / 'selected.csv'

    # Load classifier model, classify, dump noise.
    existing_classifier = load(MODEL_PATH)
    classifier = Classifier(params=None, grid_search=False, use_model=True)
    noiseless_data = classifier.classify(use_model=True, 
                        existing_model=existing_classifier, 
                        blind_data=path)

    # Generate a match matrix, some preprocessing.
    noiseless_data = noiseless_data.applymap(lower_case())
    noiseless_data['TEXT'] = noiseless_data['TEXT'].apply(remove_punctuation)
    regex_list = regex_importer()
    match_matrix = match_matricizer(noiseless_data, regex_list)
    # Run logic on matches, populate GED attributes columns.
    conclusion_matrix = populate_conclusions(match_matrix)
    return conclusion_matrix

if __name__ == "__main__":
    conclusion_matrix = process_data(data='blind')
    conclusion_matrix['CFREF'] = conclusion_matrix['CFREF'].str.upper()
    save_path = DATA_PATH / 'outputs' / 'all.csv'
    print(conclusion_matrix)
