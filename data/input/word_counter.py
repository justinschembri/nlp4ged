import pandas as pd

data_dir = "/Users/justin/Code/nlp4ged/data/input/complete_unclassified.xlsx"

data = pd.read_excel(data_dir,sheet_name=None)
year_range = range(3,22)
# translation_map = {"05":5, "06":6, "07":7, "08":8, "09":9, "10":10,
#                    "11":11, "12":12, "13":13, "14":14, "15":15, "16":16,
#                    "17":17, "18":18, "19":19, "20":20, "21":21}
word_counter = {key: [0,0] for key in year_range}

for key in data.keys():
    df = data[key] #dataframe
    #extract year / coerce to int

    for idx in df.index:
        try:
            yr = int(df['CFRef'][idx][-2:])
            sentence = df['TEXT'][idx]
            sentence_len = len(sentence.split())
        except:
            pass
    # add +1 to list entry[1]
        word_counter[yr][0] +=1
        word_counter[yr][1] += sentence_len

    #next
import csv
with open("data.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=word_counter.keys())

# Write the header row
    writer.writeheader()

# Write the data
    writer.writerow(data)
