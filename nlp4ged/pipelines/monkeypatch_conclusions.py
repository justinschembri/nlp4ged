from config import DATA_PATH, MODEL_PATH
from joblib import load
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
from nlp4ged.support.text_processing import lower_case, remove_punctuation
from nlp4ged.logic.conclusion_populater import populate_conclusions
from nlp4ged.pipelines.classification import Classifier
import pandas as pd
import numpy as np

noiseless_data_path = "/Users/justin/Code/nlp4ged/nlp4ged/noiseless_data.xlsx"
noiseless_data = pd.read_excel(noiseless_data_path)
regex_list = regex_importer()
match_matrix = match_matricizer(noiseless_data, regex_list)
conclusion_matrix = populate_conclusions(match_matrix)
a = len(conclusion_matrix)
b = len(conclusion_matrix[conclusion_matrix["PATTERN"] > 0])
b/a
conclusion_matrix[conclusion_matrix["PATTERN"] == 24]
x = conclusion_matrix[conclusion_matrix["PATTERN"] == 22]
len(x)
conclusion_matrix