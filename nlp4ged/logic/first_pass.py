import pandas as pd
from nlp4ged.regex.matchmaker import regex_importer, match_matricizer
import nlp4ged.support.text_processing as preprocess
from nlp4ged.logic.second_pass import second_pass

def logic_0(text, match_obj, cfref):
    # FIRST PASS LOGIC
    # If match (implicit), return YoC:
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc}
    # If match_obj.groupdict() has a non-None value, basement present.
    for key in match_obj.groupdict():
        if match_obj[key]:
            conclusion_dict |= {"BASEMENTS":True}
    # SECOND PASS LOGIC
    conclusion_dict |= second_pass(text, regex=r"on (\w+) floors", count=True)
    conclusion_dict |= second_pass(text, regex=r"(\w+) storey", count=True)
    conclusion_dict |= second_pass(text, regex=r"over (\w+) floors", count=True)

    return conclusion_dict

def logic_1(text, match_obj, cfref):
    # FIRST PASS LOGIC
    # If match (implicity), return YoC:
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc}
    #MATCH GROUP LOGIC
    for value in match_obj.groupdict().values():
        if value:
            conclusion_dict |= {"BASEMENTS":True}
    return conclusion_dict

def logic_2(text, match_obj, cfref):
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc}
    #MATCH GROUP LOGIC
    for value in match_obj.groupdict().values():
        if value:
            conclusion_dict |= {"BASEMENTS":True}
    # SECOND PASS LOGIC
    conclusion_dict |= second_pass(text, regex=r"(\w+) overlying", count=True)
    return conclusion_dict

def logic_3(text, match_obj, cfref):
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "CLASS":'Residential'}
    # MATCH GROUP LOGIC
    for value in match_obj.groupdict().values():
        if value:
            conclusion_dict |= {"BASEMENTS":True}
    # SECOND PASS LOGIC
    conclusion_dict |= second_pass(text, regex=r"over (\w+) floors", count=True)
    return conclusion_dict

def logic_4(text, match_obj, cfref):
    yoc = 2000 + int(cfref[-2:])
    conclusion_dict = {"YOC":yoc, "CLASS":'Residential'}
    # MATCH GROUP LOGIC
    for value in match_obj.groupdict().values():
        if value:
            conclusion_dict |= {"BASEMENTS":True}
    return conclusion_dict

def logic_5(text, match_obj, cfref):
    #MATCH GROUP LOGIC: Nil
    #SECOND PASS LOGIC
    conclusion_dict = {}
    conclusion_dict = second_pass(text, regex=r'(\w+)\s+floor(\s\w+){0,5}\s(\w+)\s(additional floor)',
                                  ordinal_then_strnum=True)
    return conclusion_dict

def first_pass_conclusions(match_key, match_obj, text, cfref):
    logic_map = {0: logic_0(text, match_obj, cfref),
                 1: logic_1(text, match_obj, cfref),
                 2: logic_2(text, match_obj, cfref),
                 3: logic_3(text, match_obj, cfref),
                 4: logic_4(text, match_obj, cfref),
                 5: logic_5(text, match_obj, cfref)}
    return logic_map[match_key]



