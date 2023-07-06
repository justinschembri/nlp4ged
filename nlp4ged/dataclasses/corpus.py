import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

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

PERMIT_REF_HEADER = 'cfref'
TEXT_HEADER = 'text'
TAG_HEADER = 'tag'

class Corpus(pd.DataFrame):
    """
    A dataframe subclass consisting of a 2 or 3 dimensional pandas dataframe.
    enforces strict construction of a dataframe-like Corpus class. 
    corpus objects are constructed from external data-sources, namely .xlsx
    files with mandatory headings. 

    Column Headings
    ===============
    Mandatory
    CFRef:  Planning reference number.
    Text:   Text description of planning permit.

    Optional
    Tag:    A classifier tag.
    """

    def __init__(self, file_path: Path):
        # Check correct filetype:
        if file_path.suffix not in ('.xlsx', '.xls'):
            error = 'Incorrect filetype, expected .xlsx/xls.'
            raise ValueError(error)
        df = pd.read_excel(file_path, header=0, sheet_name=None)
        # Handle multisheet files by concatinating:
        if isinstance(df, dict):
            df = pd.concat(df, ignore_index=True).dropna(how='all')
        # Lowercase existing columns for flexibility:
        df.columns = [col.lower() for col in df.columns]
        # Check if cfref and text are headers in the dataframe:
        minimum_headers = [PERMIT_REF_HEADER, TEXT_HEADER]
        all_headers = minimum_headers + [TAG_HEADER]
        if not all(col in df.columns for col in minimum_headers):
            error = 'Cfref and text must be present and headers in xlsx file.'
            raise ValueError(error)
        if 'tag' in df.columns:
            df = df.drop(columns=[col for col in df.columns if col 
                               not in all_headers])
            is_tagged = True
        else:
            df = df.drop(columns=[col for col in df.columns if 
                               col not in minimum_headers])
            is_tagged = False
        df = df.dropna(how='all')
        super().__init__(data=df)
        self.is_tagged = is_tagged
        self.file_path = file_path
