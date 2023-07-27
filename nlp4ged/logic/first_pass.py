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

def logic_pattern_1_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":5}
    # # #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":6}
    #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":7}
    #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":8}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_7(text:str, match_obj: re.Match, cfref:str):
    # #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":9}
    #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_9(text:str, match_obj: re.Match, cfref:str):
    # #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":10}
    #2nd pass
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_10(text:str, match_obj: re.Match, cfref:str):
    # #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":11}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_11(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":12}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_12(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":13}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_13(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":14}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_14(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":15}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_15(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":16}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def first_pass_conclusions(match_key, match_obj, text, cfref):
    logic_map = {0: logic_pattern_0_1(text, match_obj, cfref),
                 1: logic_pattern_0_2(text, match_obj, cfref),
                 2: logic_pattern_0_3(text, match_obj, cfref),
                 3: logic_pattern_0_4(text, match_obj, cfref),
                 4: logic_pattern_1_1(text, match_obj, cfref),
                 5: logic_pattern_1_2(text, match_obj, cfref),
                 6: logic_pattern_1_4(text, match_obj, cfref),
                 7: logic_pattern_1_6(text, match_obj, cfref),
                 8: logic_pattern_1_7(text, match_obj, cfref),
                 9: logic_pattern_1_9(text, match_obj, cfref),
                 10: logic_pattern_1_10(text, match_obj, cfref),
                 11: logic_pattern_1_11(text, match_obj, cfref),
                 12: logic_pattern_1_12(text, match_obj, cfref),
                 13: logic_pattern_1_13(text, match_obj, cfref),
                 14: logic_pattern_1_14(text, match_obj, cfref),
                 15: logic_pattern_1_15(text, match_obj, cfref),
                 }
    return logic_map[match_key]



