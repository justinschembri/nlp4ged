from typing import List
import string

def lower_case():
    """Lowercasing function for use with apply or applymap."""
    data_lower = lambda doc: doc.lower() if isinstance(doc, str) else doc
    return data_lower

def remove_third_party(text:str):
    new_text = text.replace("third party", "")
    return new_text

def replace_numeric_oridinals(text:str):
    new_text = text
    numeric_ordinals = ["1st", "2nd", "3rd", "4th", "5th",
                        "6th", "7th", "8th", "9th"]
    string_ord = ["first", "second", "third", "fourth", "fifth",
                        "sixth", "seventh", "eighth", "ninth"]
    ordinals_map = dict(zip(numeric_ordinals, string_ord))

    for numeric_ordinal in ordinals_map:
        new_text = new_text.replace(numeric_ordinal, ordinals_map[numeric_ordinal])
    return new_text

def replace_multiple(text:str, words:List[str]):
    """Leave only one occurance of a word in a given string."""
    new_text = text
    for word in words:
        word_count = text.count(word)
        if word_count > 1:
            new_text = text.replace(word, "", word_count-1)
    return new_text

def remove_punctuation(text:str):
    """Remove punctuation characters"""
    new_text = text
    new_text = new_text.translate(str.maketrans('','',string.punctuation))
    return new_text
