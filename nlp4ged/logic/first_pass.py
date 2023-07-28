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

def logic_pattern_1_17(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":17}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_18(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":18}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_19(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":19}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_3_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":20}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_3_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":21}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_3_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":22, "OCCUPANCY":["Commercial"]}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    return conclusion_dict

def logic_pattern_3_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":23, "OCCUPANCY":["Commercial"]}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    return conclusion_dict

def logic_pattern_4_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":24}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_4_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":25}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_4_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":26}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_4_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":27}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_4_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":28}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_4_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":29}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":30}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":31}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":32}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":33}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":34}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_6_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":35}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = building_height_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_7_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":36}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_7_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":37}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_7_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":38}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_8_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":39}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_8_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":40}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_8_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":41}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_8_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":42}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_8_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":43}
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
                 16: logic_pattern_1_17(text, match_obj, cfref),
                 17: logic_pattern_1_18(text, match_obj, cfref),
                 18: logic_pattern_1_19(text, match_obj, cfref),
                 19: logic_pattern_3_1(text, match_obj, cfref),
                 20: logic_pattern_3_2(text, match_obj, cfref),
                 21: logic_pattern_3_3(text, match_obj, cfref),
                 22: logic_pattern_3_4(text, match_obj, cfref),
                 23: logic_pattern_4_1(text, match_obj, cfref),
                 24: logic_pattern_4_2(text, match_obj, cfref),
                 25: logic_pattern_4_3(text, match_obj, cfref),
                 26: logic_pattern_4_4(text, match_obj, cfref),
                 27: logic_pattern_4_5(text, match_obj, cfref),
                 28: logic_pattern_4_6(text, match_obj, cfref),
                 29: logic_pattern_6_1(text, match_obj, cfref),
                 30: logic_pattern_6_2(text, match_obj, cfref),
                 31: logic_pattern_6_3(text, match_obj, cfref),
                 32: logic_pattern_6_4(text, match_obj, cfref),
                 33: logic_pattern_6_5(text, match_obj, cfref),
                 34: logic_pattern_6_6(text, match_obj, cfref),
                 35: logic_pattern_7_1(text, match_obj, cfref),
                 36: logic_pattern_7_2(text, match_obj, cfref),
                 37: logic_pattern_7_3(text, match_obj, cfref),
                 38: logic_pattern_8_1(text, match_obj, cfref),
                 39: logic_pattern_8_2(text, match_obj, cfref),
                 40: logic_pattern_8_3(text, match_obj, cfref),
                 41: logic_pattern_8_4(text, match_obj, cfref),
                 42: logic_pattern_8_5(text, match_obj, cfref),
                 }
    return logic_map[match_key]



