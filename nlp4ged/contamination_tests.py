import pandas as pd
from config import DATA_PATH
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
from nlp4ged.analysis.contamination import calculate_contamination
from nlp4ged.support.text_processing import lower_case

"""
A testing ground for generating contamination matrices while developing your 
regex patterns. Folder location is fixed through hardcoded declaration.
"""
# Import selected classified and clustered data.

path = DATA_PATH / 'output' / 'sample_2_classified_and_clustered.xlsx'

data = pd.read_csv(path, header=0, index_col=0)
data = data.applymap(lower_case())

regexes = regex_importer()

# Run through regex list and generate contamination matrix.

if __name__ == "__main__":
    matched_matrix = match_matricizer(data, regexes)
    calculate_contamination = calculate_contamination(matched_matrix, regexes)
    print(calculate_contamination)
