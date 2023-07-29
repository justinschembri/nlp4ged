from nlp4ged.logic.first_pass import first_pass_conclusions

def populate_conclusions(match_matrix):
    conclusion_matrix = match_matrix.copy()
    # The GED attribute is appended to the match matrix.
    attribute_list = ['CFREF', 'text', 'CLUSTER', 'MATCHES', 'HEX', 'HEX+',
                      'BASEMENTS', 'YOC', 'YOR', 'PATTERN', 'OCCUPANCY', 'text2']
    conclusion_matrix = conclusion_matrix.reindex(columns=attribute_list)
    conclusion_matrix['HEX'] = 0
    conclusion_matrix['HEX+'] = 0 
    conclusion_matrix['YOC'] = 0
    conclusion_matrix['YOR'] = 0
    conclusion_matrix['PATTERN'] = 0
    conclusion_matrix['OCCUPANCY'] = "Unknown"
    # The 'MATCHES' column in the conclusion_matrix contains a list of all regex
    # matches made.
    for idx, match_list in conclusion_matrix['MATCHES'].items():
        if match_list == []:
            continue
        for match in match_list:
            for match_key, match_obj in match.items():
                text = conclusion_matrix.at[idx,"text2"]
                cfref = conclusion_matrix.at[idx, "CFREF"]
                conclusion_dict = first_pass_conclusions(match_key, match_obj, text, cfref)
                for key in conclusion_dict:
                    if type(conclusion_matrix.at[idx, key]) == int:
                        conclusion_matrix.at[idx, key] = conclusion_matrix.at[idx, key] + conclusion_dict[key]
                    else: conclusion_matrix.at[idx, key] = conclusion_dict[key]
    return conclusion_matrix