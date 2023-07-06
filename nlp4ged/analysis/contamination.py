import pandas as pd

def calculate_contamination(match_matrix, regex_list) -> pd.DataFrame:

    cluster_range = range(match_matrix['CLUSTER'].max())
    pattern_range = range(len(regex_list))
    contamination_matrix = pd.DataFrame(columns=pattern_range,index=cluster_range)
    for cluster_ref in cluster_range:
        data_2 = match_matrix[match_matrix["CLUSTER"] == cluster_ref]
        for pattern_ref in pattern_range:
            count = 0
            for match in data_2["MATCHES"]:
                for match_dict in match:
                    if pattern_ref in match_dict:
                        count += 1
                ratio = round((count/len(data_2)),2)
            contamination_matrix.at[cluster_ref, pattern_ref] = ratio
    return contamination_matrix