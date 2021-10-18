"""
This module process and export data to a local folder in a computer
"""
import pandas as pd
from TextAnalysis_ProjectHero.date_cleaning import set_date
from TextAnalysis_ProjectHero.text_cleaning import process_text

def split_half(slice):
    """This function slpit dataframe into two smaller dataframes based on the date associated with each row

    Parameters
    ----------
    slice : dataframe
        Name of the dataframe that needs splitting
        

    Returns
    -------
    slice : 1st smaller dataframe
    slice_b : 2nd smaller dataframe

    
    """
    slice = set_date(slice)
    slice ['Date'] = pd.to_datetime(slice['Date'])
    col_names = ['Date','Label','Text Extract','Processed']
    slice = slice[col_names]
    max_date =  slice['Date'].max()
    min_date = slice['Date'].min()
    split_day = min_date + (max_date-min_date)//2
    slice_b = slice[slice['Date']>split_day]
    slice = slice[slice['Date']<= split_day]
    return slice,slice_b

def export_16(text_col,processed_col,input_filepath, output_filepath,country):
    """This function takes in a file with 8 different sheets containing extracted text.
    It will perform mulitple steps to clean the extracted text and split each sheet into two smaller sheets.
    Then export them individual to a local folder on computer

    Parameters
    ----------
    text_col : string
        Name of the text column that needs processing
        
    processed_col : string
        Name of the empty column where processed text will be stored 
        
    input_filepath : string
        Location of the input file
        
    output_filepath : string
        Location of the output file

    country : string
        Which country's data is being processed
        

    Returns
    -------
    value : True
        Returns True if the process is successfully run
    """
    processed_list_8 = process_text(text_col,processed_col,input_filepath)
    processed_list_16 = []
    for name in processed_list_8:
        name,_ = split_half(name)
        processed_list_16.append(name)
        processed_list_16.append(_)
    
    for i in range(len(processed_list_16)):
        processed_list_16[i].to_excel(output_filepath + country +'_processed_'+str(i+1)+'.xlsx',index=False)
    return True

def to_workbook(country,input_filepath,output_filepath,engine):
    """

    Parameters
    ----------
    country : string
        Name of the country where its data is being processed
        
    input_filepath : string
        Location of the input file

    output_filepath : string
        Location of the output file

    engine : string
        

    Returns
    -------
    value : True
        Returns True if the process is successfully run

    """
    xls  = pd.ExcelFile(input_filepath)
    processed_list = []
    for name in xls.sheet_names:
        name = xls.parse(name)
        processed_list.append(name)
    writer = pd.ExcelWriter(output_filepath, engine=engine)
    frames = {}
    for i in range(len(processed_list)):
        frames[country+str(i+1)] = processed_list[i]
    for sheet, frame in frames.item():
        frame.to_excel(writer,sheet_name=sheet)
    writer.save()
    return True



