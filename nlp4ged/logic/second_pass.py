import re

# def second_pass(text:str, 
#                 regex:str=None, 
#                 count:bool=None, 
#                 deduction_type:str=None,
#                 ordinal_then_strnum:bool=None):

#     regex_match = re.search(regex, text)
#     if regex_match == None:
#         return {}
    
#     capture_group_tuple = regex_match.groups()

#     def additive_count(capture_group=capture_group_tuple):
#         """Treat captured groups as integer values and add them."""
#         if capture_group_tuple == None:
#             return {'HEX':0}
#         else:
#             text_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
#                         "seven":7, "eight":8, "nine":9}
#             result = 0
#             for capture in capture_group:
#                 try:
#                     result += int(capture)
#                 except:
#                     pass
#                 if capture in text_map:
#                     integer_repr = text_map[capture]
#                     result += integer_repr
#             conclusion_dict = {'HEX':result}
#             return conclusion_dict

#     def presence_deduction(capture_group=capture_group_tuple):
#         """Make a deduction based on the presence of a statement."""
#         deduction_type_map = {"basement":("BASEMENTS", True)}
#         if capture_group != None:
#             deduction_tuple = deduction_type_map[deduction_type]
#             attribute_column = deduction_tuple[0]
#             attribute_deduction = deduction_tuple[1]
#             conclusion_dict = {attribute_column, attribute_deduction}
#         return conclusion_dict

#     def ordinal_then_strnum_count(capture_group=capture_group_tuple):
#         """When a number of new floors are added to a building, and floor is defined before."""
#         if not capture_group_tuple:
#             return {'HEX':0}
#         else:
#             conclusion_dict = {}
#             ordinal_text_map = {"first":1, "second":2, "third":3, "fourth":4,
#                                 "fifth":5, "sixth":6, "seventh":7, "1st":1,
#                                 "2nd":2, "3rd":3, "4th":4, "5th":5, "6th":6, 
#                                 "7th":7}

#             text_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
#                         "seven":7, "eight":8, "nine":9}
#             result = 0
#             result_hex_plus = 0 
#             for capture in capture_group:
#                 if capture in ordinal_text_map:
#                     result += ordinal_text_map[capture] + 1
#                 if capture in text_map:
#                     result_hex_plus += text_map[capture]
#                     break
#                 if capture in ['additional floor']:
#                     result_hex_plus += 1
#             conclusion_dict = {'HEX':result+result_hex_plus, 
#                                'HEX+':result_hex_plus}
#         return conclusion_dict
    
#     if count == True:
#         conclusion_dict = additive_count()
#     elif ordinal_then_strnum == True:
#         conclusion_dict = ordinal_then_strnum_count()
    
#     return conclusion_dict

def cardinal_wordnum_to_int(word) -> int:
    """Convert the number words to and return an integer equivalent."""
    text_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
        "seven":7, "eight":8, "nine":9}
    try:
        word_as_int = text_map[word]
        return word_as_int
    except:
        return 0
    
def ordinal_to_int(word) -> int:
    """Convert the number words to and return an integer equivalent."""
    text_map = {"1st":2, "2nd":3, "3rd":4, "4th":5, "5th":6, "6th":7,
        "7th":8, "8th":9, "9th":10, "first":2, "second":3, "third":4, "fourth":5,
        "fifth":6, "sixth":7, "seventh":8, "eight":9, "ninth":10}
    try:
        word_as_int = text_map[word]
        return word_as_int
    except:
        return 0

def single_cardinal_capture_count_yoc(text:str) -> dict:
    """
    Run a series of regex (hard-coded into function) to attempt to count 
    building height in a given building permit. Regexes all designed to make capture
    of cardinal numbers. Returns a dict object which can be added to the 
    conclusion dict.
    """
    # Regexes which also add a penthouse level. Pattern breaks w/o penthouse:
    penthouse_regexes = [
        r'(?<!existing )\b(\w+)-storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'(?<!existing )\b(\w+) storey(?=.*and)(?=.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?=.*and)(?=.*setback|.*penthouse|.*receded)'
                ]
    # Regexes which do not add a penthouse level. Pattern breaks w/ penthouse:
    no_penthouse_regexes = [
        r'(?<!existing )\b(\w+)-storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'(?<!existing )(\w+) storey(?!.*and)(?!.*setback|.*penthouse|.*receded)', 
        r'over (\w+) floors(?!.*and)(?!.*setback|.*penthouse|.*receded)',
        r'at (\w+) floor$'
                ]
    for pattern in penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex+1}
            except:
                building_height = cardinal_wordnum_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height+1}
            return conclusion_dict
    for pattern in no_penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex}
            except:
                building_height = cardinal_wordnum_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height}
            return conclusion_dict
    return {"HEX":0}

def single_ordinal_capture_count_yoc(text:str) -> dict:
    """
    Run a series of regex (hard-coded into function) to attempt to count 
    building height in a given building permit. Returns a dict object which
    can be added to the conclusion dict.
    """
    # Regexes which also add a penthouse level. Pattern breaks w/o penthouse:
    penthouse_regexes = [
        r'(?:demo\w+).*(?:const\w+)(?:.*at).*(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)(?=.*setback|.*penthouse|.*receded)'
        r'(?:.*extension at).*(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)(?=.*setback|.*penthouse|.*receded)',
        r'(?:const\w+.*)from\s(?:\w+)\still\s(\w+)\sfloor(?=.*setback|.*penthouse|.*receded)'
                ]
    # Regexes which do not add a penthouse level. Pattern breaks w/ penthouse:
    no_penthouse_regexes = [
        r'(?:demo\w+).*(?:const\w+)(?:.*at).*(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)(?!.*setback|.*penthouse|.*receded)',
        r'(?:.*extension at).*(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)(?!.*setback|.*penthouse|.*receded)',
        r'(?:constru\w+|extension)\sof\s(\w+)\sfloor$',
        r'(?:.*erect)\s(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)\s(?:floor|level)(?!.*and)',
        r'(?:const\w+.*)from\s(?:\w+)\still\s(\w+)\sfloor(?!.*setback|.*penthouse|.*receded)'
                ]
    for pattern in penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex+1}
            except:
                building_height = ordinal_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height+1}
            return conclusion_dict
    for pattern in no_penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex}
            except:
                building_height = ordinal_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height}
            return conclusion_dict
    return {"HEX":0}

def occupancy_keyowrds(text:str) -> dict:
    """
    Run a series of regex (hard-coded into function) to attempt to deduce the
    occupancy type of a given permit. Returns a dict object which can be added
    to the conclusion dict.
    """
    residential_keywords = ['flat', 'apartment', 'residence', 'house', 
                            'maisonette']
    commercial_keyowrds = ['shop', 'office']
    for keyword in residential_keywords:
        occupancy_dict = {"OCCUPANCY":[]}
        if keyword in text:
            occupancy_dict["OCCUPANCY"].append("Residential")
            break
    for keyword in commercial_keyowrds:
        if keyword in text:
            occupancy_dict["OCCUPANCY"].append("Commercial")
            break
    if len(occupancy_dict["OCCUPANCY"]) == 0:
        occupancy_dict = {"OCCUPANCY":"Unknown"}
    return occupancy_dict
#TODO: Add residential / commercial / industrial keywords!

def single_ordinal_capture_count_yoR(text:str) -> dict:
    """
    Run a series of regex (hard-coded into function) to attempt to count 
    building height in a given building permit. Returns a dict object which
    can be added to the conclusion dict.
    """
    # Regexes which also add a penthouse level. Pattern breaks w/o penthouse:
    penthouse_regexes = [
        r'(?:const\w+)\s\w+\s(\w+)\sfloor\sapartment(?=.*setback|.*penthouse|.*receded)'
                        ]
    # Regexes which do not add a penthouse level. Pattern breaks w/ penthouse:
    no_penthouse_regexes = [
        r'(?:constru\w+|extension)\sof\s(\w+)\sfloor$',
        r'(?:.*erect)\s(ground|first|second|third|fourth|fifth|sixth|seventh|eight|ninth|1st|2nd|3rd|4th|5th|6th|7th|8th|9th)\s(?:floor|level)(?!.*and)',
        r'(?:const\w+|extens\w+).*(?:at)\s(\w+)\s(floor|floor level)$',
        r'(?:const\w+)\s\w+\s(\w+)\sfloor\sapartment(?!.*setback|.*penthouse|.*receded)'
                ]
    for pattern in penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex+1}
            except:
                building_height = ordinal_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height+1}
            return conclusion_dict
    for pattern in no_penthouse_regexes:
        match = re.search(pattern, text)
        if match:
            try: 
                int_hex = int(match.group(1))
                conclusion_dict = {"HEX":int_hex}
            except:
                building_height = ordinal_to_int(match.group(1))
                conclusion_dict = {"HEX":building_height}
            return conclusion_dict
    return {"HEX":0}