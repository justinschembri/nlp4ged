import unittest
from parameterized import parameterized_class
from nlp4ged.dataclasses.corpus import Corpus
from config import DATA_PATH

# WARNING: Fixed data for trivial unittests. Do not change paths or files.
TEST_DATA_ROOT = DATA_PATH / 'tests' / 'corpus'

@parameterized_class([
    {'file_path': TEST_DATA_ROOT / 'CorpusUnitTest_CorrectData_1_untagged.xlsx',
     'expected_cols': ['cfref', 'text'],
     'expected_len': 3139,
     'expected_tag': False},
     
    {'file_path': TEST_DATA_ROOT / 'CorpusUnitTest_CorrectData_2_tagged.xlsx',
     'expected_cols': ['cfref', 'text', 'tag'],
     'expected_len': 3562,
     'expected_tag': True}
     ])

class CorpusUnitTest_CorrectData(unittest.TestCase):
    """Testing corpus class on correct datasets."""
    def test_1_data_is_correctly_imported(self):
        """
        Testing that data is properly imported, namely:
        - 'Good' data is imported and a corpus object is instantiated.
        - Expected headers are returned (for tagged / non-tagged dataset)
        - Expected length returned
        - Expected is_tagged boolean returned
        """
        corpus = Corpus(self.file_path)
        self.assertIsInstance(corpus, Corpus)
        self.assertEqual([col for col in corpus.columns], self.expected_cols)
        self.assertEqual(len(corpus), self.expected_len)
        self.assertEqual(corpus.is_tagged, self.expected_tag)

@parameterized_class([
    {'file_path': TEST_DATA_ROOT / 'CorpusUnitTest_IncorrectData_1_not_xlsx.rtf',
     'expected_exception': ValueError,
     'msg':'Incorrect filetype, expected .xlsx/xls.'},

     {'file_path': TEST_DATA_ROOT / 'CorpusUnitTest_IncorrectData_2_no_headers.xlsx',
     'expected_exception': ValueError,
     'msg':'Cfref and text must be present and headers in xlsx file.'}
     ])

class CorpusUnitTest_IncorrectData(unittest.TestCase):
    """Testing corpus clas on incorrect datasets."""
    def test_1_incorrect_data_raises_error(self):
        with self.assertRaises(self.expected_exception) as context:
            Corpus(self.file_path)
        raised_exception = context.exception
        self.assertEqual(str(raised_exception), self.msg)

if __name__ == "__main__":
    unittest.main()