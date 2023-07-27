import pandas as pd
import re
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
import nlp4ged.support.text_processing as preprocess
from nlp4ged.logic.second_pass import number_to_word, building_height_count, occupancy_keyowrds

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
    conclusion_dict = {"YOC":yoc, "PATTERN":1}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_0_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":2}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_0_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":3}
    #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_0_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":4}
    # #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def first_pass_conclusions(match_key, match_obj, text, cfref):
    logic_map = {0: logic_pattern_0_1(text, match_obj, cfref),
                 1: logic_pattern_0_2(text, match_obj, cfref),
                 2: logic_pattern_0_3(text, match_obj, cfref),
                 3: logic_pattern_0_4(text, match_obj, cfref),
                 }
    return logic_map[match_key]



