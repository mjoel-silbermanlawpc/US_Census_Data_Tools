from imports import *

from input_output import file_loader
from input_output import file_exporter


def percent_remove(df):
    """
    this function removes the 'Percent' rows from the spreadsheet:
    1. receives a df as input
    2. creates a new df, filtered_df
        a. checks a row for if the value in column[3] DOES NOT equal 'Percent'
        b. If condition (a.) is met, then that row is allowed to be in our new df (filtered_df)
    3. the new df is returned
    """
    filtered_df = df.loc[df[df.columns[3]] != 'Percent']
    print("Percent Rows removed")
    return filtered_df


def specified_remove(df, column_index, searchTerm):
    """
    this function is an improved version of percent_remove. It works the same way, except it also:
    1. allows user to specify which column to search in (column_index)
    2. which term to look for (searchTerm)
    4. then deletes the row
    5. returns the new df (filtered_df)
    """
    filtered_df = df.loc[df[df.columns[column_index]] != searchTerm]
    print("Specified remove of '", searchTerm, "' at column index", column_index, "completed.")
    return filtered_df


def index_replace(df, start_index, col_index, n, new_value):
    """
    This function allows us to increment through the df while replacing a value at given column:
    :param df: the input data frame
    :param start_index: index of df row where the replacing will start
    :param col_index: index of column to replace in
    :param n: increment of row traversing
    :param new_value: value to be put in
    :return filtered_df: the completed new df
    """

    for i in range(start_index, len(df), n):
        df.iloc[i, col_index] = new_value
    filtered_df = df
    print("Index based replacing starting at row", start_index, ", incrementing by", n, ", with value '", new_value,
          "' complete.")
    return filtered_df


def column_row_delete(df, drop_index, ax):
    """
    Function to drop a specified column or row from a DataFrame.

    :param df: input DataFrame
    :param drop_index: index of the column or row to drop
    :param ax: 0 to drop rows, 1 to drop columns
    :return: the DataFrame with the specified column or row dropped
    """
    if ax == 1:
        # Dropping a column
        filtered_df = df.drop(df.columns[drop_index], axis=ax)
        print("Column at index", drop_index, "dropped.")
    else:
        # Dropping a row
        filtered_df = df.drop(drop_index, axis=ax)
        print("Row at index", drop_index, "dropped.")

    return filtered_df.reset_index(drop=True)


def concat_dataframes(dfs):
    """
    Concatenate a list of DataFrames vertically and reset the index.

    Parameters:
    dfs (list): List of pandas DataFrames to concatenate.

    Returns:
    pd.DataFrame: Concatenated DataFrame with reset index.
    """
    df_combined = pd.concat(dfs, axis=0)

    df_combined = df_combined.reset_index(drop=True)

    return df_combined


header = ["TBLID", "GEOID", "GEONAME", "TITLE", "Total, race and ethnicity", "Hispanic or Latino", "White alone",
          "Black or African American alone", "American Indian and Alaska Native alone", "Asian alone",
          "Native Hawaiian and Other Pacific Islander alone", "Two or More", "CC", "CC Title"]

'''
# example usage:
# load the spreadsheet
activeFile = file_loader('spreadsheets/hd_m/hd_m_EEOALL1W_C21.csv', 2)
# remove percent rows
activeFile = percent_remove(activeFile)
# remove the empty 'Total, both sexes' rows
activeFile = specified_remove(activeFile,3,'Total, both sexes')
# rename the actual total row
activeFile = index_replace(activeFile, 0,3, 5,'Total')
# remove the empty 'Male' rows
activeFile = specified_remove(activeFile,3,'Male')
# rename the actual male row
activeFile = index_replace(activeFile, 1,3, 4,'Male')
# remove the empty 'Female' rows
activeFile = specified_remove(activeFile,3,'Female')
# rename the actual female row
activeFile = index_replace(activeFile, 2,3, 3,'Female')
# export the completed table
file_exporter(activeFile, 'spreadsheets/p_hd_m/p_hd_m_EEOALL1W_C21.csv', 2)

activeFile = file_loader('spreadsheets/hd_m/hd_m_EEOALL1W_P01.csv', 2)
activeFile = percent_remove(activeFile)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female')
file_exporter(activeFile, 'spreadsheets/p_hd_m/p_hd_m_EEOALL1W_P01.csv', 2)

activeFile = file_loader('spreadsheets/hd_m/hd_m_EEOALL1W_P06.csv', 2)
activeFile = percent_remove(activeFile)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female')
file_exporter(activeFile, 'spreadsheets/p_hd_m/p_hd_m_EEOALL1W_P06.csv', 2)

activeFile = file_loader('spreadsheets/hd_m/hd_m_EEOALL1W_P07.csv', 2)
activeFile = percent_remove(activeFile)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female')
file_exporter(activeFile, 'spreadsheets/p_hd_m/p_hd_m_EEOALL1W_P07.csv', 2)

activeFile = file_loader('spreadsheets/hd_m/hd_m_EEOALL1W_P10.csv', 2)
activeFile = percent_remove(activeFile)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female')
file_exporter(activeFile, 'spreadsheets/p_hd_m/p_hd_m_EEOALL1W_P10.csv', 2)

c21 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_C21.csv',2)
p01 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_P01.csv',2)
p06 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_P06.csv',2)
p07 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_P07.csv',2)
p10 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_P10.csv',2)

grouped = [c21, p01, p06, p07, p10]
total = concat_dataframes(grouped)

file_exporter(total,'spreadsheets/FINAL/FINAL_EEOALL1W_TOTAL.csv',2)
'''

'''
activeFile = file_loader('spreadsheets/Originals/EEOALL1WC_P01.csv',2)
activeFile = column_row_delete(activeFile, 20, 1)
activeFile = column_row_delete(activeFile, 18, 1)
activeFile = column_row_delete(activeFile, 16, 1)
activeFile = column_row_delete(activeFile, 14, 1)
activeFile = column_row_delete(activeFile, 12, 1)
activeFile = column_row_delete(activeFile, 10, 1)
activeFile = column_row_delete(activeFile, 8, 1)
activeFile = column_row_delete(activeFile, 6, 1)
activeFile = column_row_delete(activeFile, 3, 1)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total %')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male %')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female %')
activeFile.columns = header
file_exporter(activeFile, 'spreadsheets/FINAL/FINAL_EEOALL1WC_P01.csv',2)

activeFile = file_loader('spreadsheets/Originals/EEOALL1WC_P07.csv', 2)
activeFile = column_row_delete(activeFile, 20, 1)
activeFile = column_row_delete(activeFile, 18, 1)
activeFile = column_row_delete(activeFile, 16, 1)
activeFile = column_row_delete(activeFile, 14, 1)
activeFile = column_row_delete(activeFile, 12, 1)
activeFile = column_row_delete(activeFile, 10, 1)
activeFile = column_row_delete(activeFile, 8, 1)
activeFile = column_row_delete(activeFile, 6, 1)
activeFile = column_row_delete(activeFile, 3, 1)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total %')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male %')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female %')
activeFile.columns = header
file_exporter(activeFile, 'spreadsheets/FINAL/FINAL_EEOALL1WC_P07.csv', 2)

activeFile = file_loader('spreadsheets/Originals/EEOALL1WC_P10.csv', 2)
activeFile = column_row_delete(activeFile, 20, 1)
activeFile = column_row_delete(activeFile, 18, 1)
activeFile = column_row_delete(activeFile, 16, 1)
activeFile = column_row_delete(activeFile, 14, 1)
activeFile = column_row_delete(activeFile, 12, 1)
activeFile = column_row_delete(activeFile, 10, 1)
activeFile = column_row_delete(activeFile, 8, 1)
activeFile = column_row_delete(activeFile, 6, 1)
activeFile = column_row_delete(activeFile, 3, 1)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = column_row_delete(activeFile, 0, 0)
activeFile = specified_remove(activeFile,3,'Total, both sexes')
activeFile = index_replace(activeFile, 0,3, 5,'Total %')
activeFile = specified_remove(activeFile,3,'Male')
activeFile = index_replace(activeFile, 1,3, 4,'Male %')
activeFile = specified_remove(activeFile,3,'Female')
activeFile = index_replace(activeFile, 2,3, 3,'Female %')
activeFile.columns = header
file_exporter(activeFile, 'spreadsheets/FINAL/FINAL_EEOALL1WC_P10.csv', 2)

p01 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1WC_P01.csv')
p07 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1WC_P07.csv')
p10 = file_loader('spreadsheets/FINAL/FINAL_EEOALL1WC_P10.csv')

grouped = [p01, p07, p10]
total = concat_dataframes(grouped)

file_exporter(total,'spreadsheets/FINAL/FINAL_EEOALL1WC_TOTAL.csv',2)
'''
