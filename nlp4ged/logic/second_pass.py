import re

def second_pass(text:str, 
                regex:str=None, 
                count:bool=None, 
                deduction_type:str=None,
                ordinal_then_strnum:bool=None):

    regex_match = re.search(regex, text)
    if regex_match == None:
        return {}
    
    capture_group_tuple = regex_match.groups()

    def additive_count(capture_group=capture_group_tuple):
        """Treat captured groups as integer values and add them."""
        if capture_group_tuple == None:
            return {'HEX':0}
        else:
            text_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
                        "seven":7, "eight":8, "nine":9}
            result = 0
            for capture in capture_group:
                try:
                    result += int(capture)
                except:
                    pass
                if capture in text_map:
                    integer_repr = text_map[capture]
                    result += integer_repr
            conclusion_dict = {'HEX':result}
            return conclusion_dict

    def presence_deduction(capture_group=capture_group_tuple):
        """Make a deduction based on the presence of a statement."""
        deduction_type_map = {"basement":("BASEMENTS", True)}
        if capture_group != None:
            deduction_tuple = deduction_type_map[deduction_type]
            attribute_column = deduction_tuple[0]
            attribute_deduction = deduction_tuple[1]
            conclusion_dict = {attribute_column, attribute_deduction}
        return conclusion_dict

    def ordinal_then_strnum_count(capture_group=capture_group_tuple):
        """When a number of new floors are added to a building, and floor is defined before."""
        if not capture_group_tuple:
            return {'HEX':0}
        else:
            conclusion_dict = {}
            ordinal_text_map = {"first":1, "second":2, "third":3, "fourth":4,
                                "fifth":5, "sixth":6, "seventh":7, "1st":1,
                                "2nd":2, "3rd":3, "4th":4, "5th":5, "6th":6, 
                                "7th":7}

            text_map = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
                        "seven":7, "eight":8, "nine":9}
            result = 0
            result_hex_plus = 0 
            for capture in capture_group:
                if capture in ordinal_text_map:
                    result += ordinal_text_map[capture] + 1
                if capture in text_map:
                    result_hex_plus += text_map[capture]
                    break
                if capture in ['additional floor']:
                    result_hex_plus += 1
            conclusion_dict = {'HEX':result+result_hex_plus, 
                               'HEX+':result_hex_plus}
        return conclusion_dict
    
    if count == True:
        conclusion_dict = additive_count()
    elif ordinal_then_strnum == True:
        conclusion_dict = ordinal_then_strnum_count()
    
    return conclusion_dict


