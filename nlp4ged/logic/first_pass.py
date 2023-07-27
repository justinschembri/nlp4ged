import pandas as pd
import re
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
import nlp4ged.support.text_processing as preprocess
from nlp4ged.logic.second_pass import second_pass
from nlp4ged.logic.second_pass import number_to_word

RESIDENTIAL_KEYOWRDS = ['residential', 'apartments', 'flats']

"""
A collection of functions for deriving conclusions from a corpus, post 
de-noising.

ARGS:
    text(str): A building permit string.
    match_obj: The match object from ...
    cfref: The CFREF (Planning Permit) component.
"""

def logic_pattern_0_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "CLASS":"Residential", "PATTERN":1}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    pattern = r'on (\w+) floors(?=.*and)(?=.*setback|.*penthouse|.*receded)'
    match = re.search(pattern, text)
    if match:
        building_height = number_to_word(match.group(1))
        conclusion_dict |= {"HEX":building_height+1}
    # BH = (\w+) scenario:
    pattern = r'on (\w+) floors(?!.*and)'
    match = re.search(pattern, text)
    if match:
        building_height = number_to_word(match.group(1))
        conclusion_dict |= {"HEX":building_height}
    return conclusion_dict

def logic_pattern_0_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "CLASS":"Residential", "PATTERN":2}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    patterns = [
        r'(\w+)-storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'(\w+) storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?=.*and)(?=.*setback|.*penthouse|.*receded)'
                ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            building_height = number_to_word(match.group(1))
            conclusion_dict |= {"HEX":building_height+1}
    # BH = (\w+) scenario
    patterns = [
        r'(\w+)-storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'(\w+) storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?!.*and)(?!.*setback|.*penthouse|.*receded)'
                ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            building_height = number_to_word(match.group(1))
            conclusion_dict |= {"HEX":building_height}
    return conclusion_dict

def logic_pattern_0_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "CLASS":"Residential", "PATTERN":3}
    #2nd pass
    patterns = [
        r'(\w+)-storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'(\w+) storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?=.*and)(?=.*setback|.*penthouse|.*receded)'
                ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            building_height = number_to_word(match.group(1))
            conclusion_dict |= {"HEX":building_height+1}
    # BH = (\w+) scenario
    patterns = [
        r'(\w+)-storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'(\w+) storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?!.*and)(?!.*setback|.*penthouse|.*receded)'
                ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            building_height = number_to_word(match.group(1))
            conclusion_dict |= {"HEX":building_height}
    return conclusion_dict


def first_pass_conclusions(match_key, match_obj, text, cfref):
    logic_map = {0: logic_pattern_0_1(text, match_obj, cfref),
                 1: logic_pattern_0_2(text, match_obj, cfref),
                 2: logic_pattern_0_3(text, match_obj, cfref)}
    return logic_map[match_key]



