import pandas as pd
from sklearn.model_selection import train_test_split

"""
The CorpusImporter class handles xlsx imports.
Its attributes are PA References (CFRef), Text and Tag columns.
Splitting training data and splicing data by year ranges is also handled by the class.

Mandatory headings for XLSX imports:
- CFRef - the application reference type, in format xxxx/YY,
- TEXT - the application description.

Optional headings:
- TAG - a classifier tag,
"""
# Function handling PA references and year of permit:
def year_extract(ref):
    year = int('20' + ref[-2:]) # make good for xxxx/YY format in CFRef
    return year # new format: 20YY

class CorpusImporter:

    def __init__(self, file):
        self.file = file
        self.raw = pd.read_excel(file, 
                                sheet_name=None,
                                header=0,
                                engine='openpyxl')
        
        if isinstance(self.raw, dict):
            self.raw = pd.concat(self.raw, ignore_index=True).dropna(how='all') # make good for multisheet files.
        else:
            self.raw = self.raw.dropna(how='all') 
        
        self.ref = self.raw['CFRef'] # format xxxx/YY
        self.text = self.raw['TEXT']
        
        self.year = self.ref.map(year_extract) # new format: 20YY

        if 'TAG' in self.raw.columns:
            self.tag = self.raw['TAG']
    
    def split(self, date_range=None):
        if date_range == [['all']]:
            texts, tags = self.text, self.tag
        else:
            date_range: list
            format_translator = {5:'05', 6:'06', 7:'07', 8:'08', 9:'09', 10:'10',11:'11',12:'12',
                                13:'13', 14:'14', 15:'15', 16:'16', 17:'17', 18:'18', 19:'19', 20:'20', 21:'21', 22:'22'}
            start_year, end_year = format_translator[date_range[0][0]], format_translator[date_range[0][1]]
            start_year, end_year = year_extract(start_year), year_extract(end_year)
            year_splicer = (self.year >= start_year) & (self.year <= end_year)
            texts, tags  = self.text[year_splicer], self.tag[year_splicer]

        X_train, X_test, y_train, y_test = train_test_split(texts, tags, test_size=0.33, random_state=53)
        return X_train, X_test, y_train, y_test
