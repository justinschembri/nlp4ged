from typing import Callable
from parameterized import parameterized
import pandas as pd
import unittest
import nlp4ged.logic.first_pass as first_pass

class TestParametizer:

    def __init__(self, logic_suite=None):
        self.path = "/Users/justin/Code/nlp4ged/_data/_tests/patterns.csv"
        self.data = pd.read_csv(self.path, header=0)
        self.logic_suite = logic_suite

        def pattern_0_test_params():
            data = self.data[self.data["PATTERN"] == 0]
            texts = data['TEXT']
            expected = data['HEX']
            test_parameters = []
            for idx, text in texts.items():
                test_name = "Pattern 0 - " + str(idx+2)
                logic_answer, column = first_pass.logic_0(text)
                expect = expected[idx]
                test_tuple = (test_name, logic_answer, expect)
                test_parameters.append(test_tuple)
            return test_parameters
        
        self.function_map = {0:pattern_0_test_params}
        
    def generate_test_params(self):
        return(self.function_map[self.logic_suite]())

class LogicPerformanceTest(unittest.TestCase):

    test_parameters = TestParametizer(logic_suite=0).generate_test_params()
    @parameterized.expand(test_parameters)
    def test_logic_pattern_0(self, name, inputs, expected):
        self.assertEqual(inputs, expected)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

