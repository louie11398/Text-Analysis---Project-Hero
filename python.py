import re
from num2words import num2words
import contractions
from TextAnalysis import data_processing as dp
from TextAnalysis import date_cleaning as dc
from TextAnalysis import text_cleaning as tc
import pandas as pd



input_filepath = '/Users/louietran/Downloads/Copy of US_processed_data.xlsx'
output_filepath  = '/Users/louietran/Documents/FLE OUTPUT/'
dp.export_16('Text Extract','Processed',input_filepath, output_filepath,'US')


