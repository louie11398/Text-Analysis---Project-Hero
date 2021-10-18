"""
This module clean input text
"""
import re
from TextAnalysis_ProjectHero.date_cleaning import fill_date
from num2words import num2words
import contractions
import pandas as pd

def remove_apos_space(string):
    """Removes spaces before an apostrophy in a given text

    Parameters
    ----------
    string : string
        Text that needs processing
        

    Returns
    -------
    new_string : string
        New string without spaces before an apostrophy

    """
    for i in [string]:
        new_string = [re.sub(r'\s+\'',"'",i)]
        new_string = ''.join(new_string)
  
    return new_string

def merge_numbers(string):
    """Merge numbers that have their first digit separated from the rest by white spaces

    Parameters
    ----------
    string : string
        Text needs processing
        

    Returns
    -------
    s : string
        New string without numbers having their first digit separated from the rest by white spaces
    """
    s  = string.split()
    for i ,word in enumerate(s):
        for i in range(0,(len(s)-1)):
            if s[i].isdigit():
                current_word = s[i]
                if s[i+1].isdigit():
                    next_word = s[i+1]
                    s[i+1] = ''
                    new_word = current_word + next_word
                    s[i] = new_word
    s = ' '.join(s)
    return s

def num_to_words(string):
    """Convert numbers that are strings to words

    Parameters
    ----------
    string : string
        Text needs processing
        

    Returns
    -------
    string: string
        New string with all numbers converted to words

    """
    for word in string.split():
        if word.isdigit():
            string= string.replace(word,num2words(word))
            string = string.replace('-',' ')
    return string

def word_expand(string):
    """Expand contractions. Example: They're  --> They are

    Parameters
    ----------
    string : string
        Text needs processing
        

    Returns
    -------
    expanded_text : string
        New string with all contractions expanded

    """
    expanded_words = []
    for word in string.split():
        expanded_words.append(contractions.fix(word))
        expanded_text = ' '.join(expanded_words)
    return expanded_text

def process_text(text_col,processed_col,input_filepath):
    """Process input text with multiple processes:
        - remove spaces before an apostrophy
        - expand contractions
        - lower case
        - merge numbers have its first digit separated from the rest
        - convert numbers to words
        - delete excess white spaces

    Parameters
    ----------
    text_col : string
        Name of the text column needs processing

    processed_col :
        Name of the empty column to store the processed text

    input_filepath : string
        Location of the input file
        

    Returns
    -------
    processed_list : list
        A list of eight dataframes with theirs text column processed
    """
    xls = pd.ExcelFile(input_filepath)
    processed_list = []
    for slice in xls.sheet_names:
        slice = xls.parse(slice)
        slice = slice.dropna(subset=[text_col])
        slice[processed_col] = slice[processed_col].apply(lambda x: remove_apos_space(x))
        slice[processed_col] = slice[processed_col].apply(lambda x: word_expand(x))
        slice[processed_col] = slice[processed_col].str.lower()
        slice[processed_col] = slice[processed_col].apply(lambda x: re.sub('[^a-z0-9]+',' ',x))
        slice[processed_col] = slice[processed_col].apply(lambda x: merge_numbers(x))
        slice[processed_col] = slice[processed_col].apply(lambda x: num_to_words(x))
        slice[processed_col] = slice[processed_col].apply(lambda x: ' '.join(x.split()))
        slice = fill_date(slice,'Date')
        processed_list.append(slice)
    return processed_list

