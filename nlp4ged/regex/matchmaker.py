import numpy as np
import re
import csv

# rootFolder = os.path.dirname(str(pathlib.Path(sys.argv[0]).resolve()))
# path = rootFolder + '/regex/regex_list.csv'
folder = "/Users/justin/Code/nlp4ged/nlp4ged/regex"
file = '/regex_list.csv'
path = folder + file
def regex_importer() -> list:
    """Import regex suite."""
    regex_list = {}
    with open(path, newline="") as csvfile:
        regex_reader = csv.reader(csvfile,delimiter="\n")
        for idx, regex in enumerate(regex_reader):
            regex_pattern = {idx:regex[0]}
            regex_list |= regex_pattern
    return regex_list

def match_matricizer(data, regexes):
    """
    Generate the match matrix, a modified version of the dataset with a 'matches'
    column. This column contains a list of int corresponding to a regex match.
    """
    data['MATCHES'] = np.empty((len(data), 0)).tolist()
    def regex_match(text:str, pattern:str) -> int:
        regex = re.compile(pattern)
        match = re.search(regex, text)
        if match != None:
            return match

    for ref, pattern in regexes.items():
        for idx, text in data['TEXT'].items():
            match = regex_match(text, pattern)
            if match != None:
                data.at[idx,'MATCHES'].append({ref:match})
    return data