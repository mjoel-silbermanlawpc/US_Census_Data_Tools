import pandas as pd


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


def specified_remove(df, column_index, search_term):
    """
    this function is an improved version of percent_remove. It works the same way, except it also:
    1. allows user to specify which column to search in (column_index)
    2. which term to look for (searchTerm)
    4. then deletes the row
    5. returns the new df (filtered_df)
    """
    filtered_df = df.loc[df[df.columns[column_index]] != search_term]
    print("Specified remove of '", search_term, "' at column index", column_index, "completed.")
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


def add_custom_columns(df, x, i, n, prefix):
    """
    Adds empty columns to a DataFrame starting from column x, every i columns, n times.

    Parameters:
        df (pd.DataFrame): The DataFrame to modify.
        x (int): The starting column index.
        i (int): The interval at which to add new columns.
        n (int): The total number of new columns to add.
        prefix (str): The string to add before the name of the column to the left.

    Returns:
        pd.DataFrame: The modified DataFrame with new empty columns.
    """
    new_columns = []
    col_pos = x
    for _ in range(n):
        new_col_name = prefix + df.columns[col_pos]
        new_columns.append((col_pos, new_col_name))
        col_pos += (i + 1)

    for pos, col_name in new_columns:
        df.insert(pos, col_name, None)

    return df


def add_shifted_column(df, index, prefix, shift_row, shift_col):
    """
    This function allows us to insert a new column at a specified position in the DataFrame.
    The values for the new column are taken from a specified row and column offset relative
    to the position of the new column.

    :param df: DataFrame to manipulate
    :param index: Position at which to insert the new column (1-based index)
    :param prefix: Prefix to use for the new column's name, which is derived from the column to its left
    :param shift_row: Number of rows to shift for the fill value (positive for down, negative for up)
    :param shift_col: Number of columns to shift for the fill value (positive for right, negative for left)
    :return: Modified DataFrame with the new column inserted
    """
    if index < 1 or index > len(df.columns):
        raise IndexError("Index out of bounds")

    left_col_name = df.columns[index - 1]
    new_col_name = f"{prefix}{left_col_name}"
    new_col = [None] * len(df)

    for i in range(len(df)):
        shifted_row = i + shift_row
        shifted_col = index - 1 + shift_col
        if 0 <= shifted_row < len(df) and 0 <= shifted_col < len(df.columns):
            new_col[i] = df.iloc[shifted_row, shifted_col]

    df.insert(index, new_col_name, new_col)
    print("New column at index", index, "added, with prefix '", prefix, "'. Row adjustment of", shift_row,
          "and column adjustment of", shift_col, "for fill value.")

    return df


def sum_and_flatten(df, start, end, geo_list):
    '''
    This function essentially converts a multiple row df into a single row one, by summing select columns and concatenating others.
    :param df: input df, usually more than 1 row
    :param start: column to start summing
    :param end: last column to sum
    :param geo_list: list of geonames
    :return: the new flattened df, df_copy
    '''

    df_copy = df.copy()

    for col in df_copy.columns[start:end + 1]:
        col_sum = df_copy[col].sum()
        df_copy.at[0, col] = col_sum

    df_copy = df_copy.iloc[[0]]
    new_geoname = " | ".join(geo_list)
    df_copy.iloc[0, df_copy.columns.get_loc('GEONAME')] = new_geoname

    return df_copy


def avg_and_flatten(df, start, end, geo_list):
    '''
    This function converts a multiple row percentage df into a single row one, by taking the average percentage of some columns and concatenating others.
    :param df: input df, usually more than 1 row
    :param start: column to start averaging
    :param end: last column to average
    :param geo_list: list of geonames
    :return: the new flattened averaged df, df_copy
    '''

    df_copy = df.copy()

    for col in df_copy.columns[start:end + 1]:
        col_sum = df_copy[col].sum()
        df_copy.at[0, col] = col_sum / len(geo_list)

    df_copy = df_copy.iloc[[0]]
    new_geoname = " | ".join(geo_list)
    df_copy.iloc[0, df_copy.columns.get_loc('GEONAME')] = new_geoname

    return df_copy


def df_to_percentages(df, start_idx, end_idx):
    '''
    This function turns an input df of raw numbers into one of percentages. It divides select columns by the total, and adds a percent symbol to column names.
    :param df: input df, must be 1 row
    :param start_idx: where to start the dividing
    :param end_idx: where to end the dividing
    :return: df_copy, the new df
    '''
    df_copy = df.copy()
    total_value = df_copy.iat[0, 3]
    for col in df_copy.columns[start_idx:end_idx + 1]:
        df_copy[col] = df_copy[col].astype('float64')
        df_copy.at[df_copy.index[0], col] = (df_copy.at[df_copy.index[0], col] / total_value) * 100

    # Add '%' to the header row labels
    new_columns = []
    for i, col in enumerate(df_copy.columns):
        if start_idx <= i <= end_idx:
            new_columns.append(f"{col} %")
        else:
            new_columns.append(col)
    df_copy.columns = new_columns

    return df_copy


def apply_weights(df, start_idx, end_idx, weight_list, mode=1):
    '''
    this function applies the user input weights to the input df. The weights have already been validated, so all it must do is iterate through and multiply weights.
    :param df: input df (must be length of weight list)
    :param start_idx: column of where to start weighting
    :param end_idx: column where to end weighting
    :param weight_list: list of weights
    :param mode: apply weights to percentage or raw
    :return:new weighted df, df_copy
    '''
    df_copy = df.copy()

    if len(weight_list) != len(df_copy):
        raise ValueError("Length of weight_list must match the number of rows in the DataFrame")

    if mode == 1:
        n = len(weight_list)
    if mode == 2:
        n = 1

    for i, weight in enumerate(weight_list):
        # Multiply by weight*n and cast to float to avoid dtype issues
        df_copy.iloc[i, start_idx:end_idx + 1] = (df_copy.iloc[i, start_idx:end_idx + 1] * weight * n).astype(float)

    return df_copy


header = ["TBLID", "GEOID", "GEONAME", "TITLE", "Total, race and ethnicity", "Hispanic or Latino", "White alone",
          "Black or African American alone", "American Indian and Alaska Native alone", "Asian alone",
          "Native Hawaiian and Other Pacific Islander alone", "Two or More", "CC", "CC Title"]
