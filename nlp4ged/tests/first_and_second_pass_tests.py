import pandas as pd
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
from nlp4ged.logic.conclusion_populater import populate_conclusions
import unittest

# Test text, should match to pattern 0.
class PatternTests(unittest.TestCase):
    def test_pattern_0_a(self):
        text = "to construct a terraced house and underlying garage"
        regex_list = regex_importer()
        data_1 = {"CFREF":"00123/22",
                "TEXT": text,
                "CLUSTER": [0]}
        data_1 = pd.DataFrame(data_1)
        match_matrix_1 = match_matricizer(data_1, regex_list)
        conclusion_matrix = populate_conclusions(match_matrix_1)

        yoc_expected = 2022
        yoc_result = conclusion_matrix.at[0, "YOC"]
        basements_expected = True
        basements_result = conclusion_matrix.at[0,"BASEMENTS"]
        expected = [yoc_expected, basements_expected]
        results = [yoc_result, basements_result]

        self.assertEqual(expected, results)

    def test_pattern_0_b(self):
        text = "demolition of existing store to construct a terraced house on four floors with washroom at roof level and domestic store at basement level"
        regex_list = regex_importer()
        data_1 = {"CFREF":"00123/22",
                "TEXT": text,
                "CLUSTER": [0]}
        data_1 = pd.DataFrame(data_1)
        match_matrix_1 = match_matricizer(data_1, regex_list)
        conclusion_matrix = populate_conclusions(match_matrix_1)

        yoc_expected = 2022
        hex_expected = 4
        basements_expected = True

        yoc_result = conclusion_matrix.at[0, "YOC"]
        basements_result = conclusion_matrix.at[0,"BASEMENTS"]
        hex_result = conclusion_matrix.at[0,"HEX"]

        expected = [yoc_expected, basements_expected, hex_expected]
        results = [yoc_result, basements_result, hex_result]

        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main(verbosity=2)
