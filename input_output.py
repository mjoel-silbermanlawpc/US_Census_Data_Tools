from imports import *

def file_loader(filepath, mode, header_option=None):
    """
    Load a file (xlsx or csv) and return a DataFrame.

    Parameters:
    filepath (str): The path to the file.
    mode (int): 1 for xlsx, otherwise csv.
    header_option (int or None): Specify 0 to use the first row as the header, or None if there is no header.
                                 Default is None, which assumes there is no header.

    Returns:
    DataFrame or None: Loaded DataFrame, or None if an error occurs.
    """
    if mode == 1:  # Load xlsx file
        try:
            df = pd.read_excel(filepath, header=header_option)
        except Exception as e:
            print(f"An error occurred while loading xlsx file: {e}")
            return None
    else:  # Load csv file
        try:
            df = pd.read_csv(filepath, header=header_option, low_memory=False, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(filepath, header=header_option, low_memory=False, encoding='latin1')
        except Exception as e:
            print(f"An error occurred while loading csv file: {e}")
            return None

    print(df)
    return df


def file_exporter(df, filepath, mode):
    """
    This function:
    1. Takes input of a data frame and file location
    2. Exports the data frame to a xlsx file
    3. Handles any exceptions that may occur during the export process
    4. No return
    """
    if mode == 1 :
        try:
            df.to_excel(filepath, header=True, index=False)
            print(f"Data frame successfully exported to {filepath}")
        except Exception as e:
            print(f"An error occurred while exporting the data frame: {e}")
    if mode == 2:
        try:
            df.to_csv(filepath, header=True, index=False)
            print(f"Data frame successfully exported to {filepath}")
        except Exception as e:
            print(f"An error occurred while exporting the data frame: {e}")

