import pandas as pd
import re
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
import nlp4ged.support.text_processing as preprocess
from nlp4ged.logic.second_pass import cardinal_wordnum_to_int, single_cardinal_capture_count, occupancy_keyowrds, single_ordinal_capture_count

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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_0_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":3}
    #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_0_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":4}
    # #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":5}
    # # #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":6}
    #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":7}
    #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_1_9(text:str, match_obj: re.Match, cfref:str):
    # #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":10}
    #2nd pass
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
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

def logic_pattern_9_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":44}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_9_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":45}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_9_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":46}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_9_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":47}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_9_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":48}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":49}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":50}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":51}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":52}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":53}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":54}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_12_7(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":55}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_13_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":56}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_13_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":57}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_13_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":58}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_14_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":59}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":60}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":61}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":62}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":63}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":64}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_15_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":65}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":66}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":67}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_4(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":68}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_5(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":69}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_6(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":70}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_16_7(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yor = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOR":yor, "PATTERN":71}
    #2nd pass
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_17_1(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":72}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_17_2(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":73}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
    occupancy_dict = occupancy_keyowrds(text)
    conclusion_dict |= occupancy_dict
    return conclusion_dict

def logic_pattern_17_3(text:str, match_obj: re.Match, cfref:str):
    #1st pass
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "PATTERN":74}
    #2nd pass
    if "basement" in text:
        conclusion_dict |= {"BASEMENTS":True}
    # BH = (\w+) plus penthouse scenario
    hex_dict = single_cardinal_capture_count(text)
    if hex_dict["HEX"] == 0:
        hex_dict = single_ordinal_capture_count(text)
    conclusion_dict |= hex_dict
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
                 43: logic_pattern_9_1(text, match_obj, cfref),
                 44: logic_pattern_9_2(text, match_obj, cfref),
                 45: logic_pattern_9_3(text, match_obj, cfref),
                 46: logic_pattern_9_4(text, match_obj, cfref),
                 47: logic_pattern_9_5(text, match_obj, cfref),
                 48: logic_pattern_12_1(text, match_obj, cfref),
                 49: logic_pattern_12_2(text, match_obj, cfref),
                 50: logic_pattern_12_3(text, match_obj, cfref),
                 51: logic_pattern_12_4(text, match_obj, cfref),
                 52: logic_pattern_12_5(text, match_obj, cfref),
                 53: logic_pattern_12_6(text, match_obj, cfref),
                 54: logic_pattern_12_7(text, match_obj, cfref),
                 55: logic_pattern_13_1(text, match_obj, cfref),
                 56: logic_pattern_13_2(text, match_obj, cfref),
                 57: logic_pattern_13_3(text, match_obj, cfref),
                 58: logic_pattern_14_1(text, match_obj, cfref),
                 59: logic_pattern_15_1(text, match_obj, cfref),
                 60: logic_pattern_15_2(text, match_obj, cfref),
                 61: logic_pattern_15_3(text, match_obj, cfref),
                 62: logic_pattern_15_4(text, match_obj, cfref),
                 63: logic_pattern_15_5(text, match_obj, cfref),
                 64: logic_pattern_15_5(text, match_obj, cfref),
                 65: logic_pattern_16_2(text, match_obj, cfref),
                 66: logic_pattern_16_3(text, match_obj, cfref),
                 67: logic_pattern_16_4(text, match_obj, cfref),
                 68: logic_pattern_16_5(text, match_obj, cfref),
                 69: logic_pattern_16_6(text, match_obj, cfref),
                 70: logic_pattern_16_7(text, match_obj, cfref),
                 71: logic_pattern_17_1(text, match_obj, cfref),
                 72: logic_pattern_17_2(text, match_obj, cfref),
                 73: logic_pattern_17_3(text, match_obj, cfref),
                 }
    return logic_map[match_key]



