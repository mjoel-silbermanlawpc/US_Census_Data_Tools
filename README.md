# US Census Data Tools
## Matthew Joel | Silberman Law PC
This repository contains a suite of tools designed for handling US Census data. It includes functions for importing/exporting data, cleaning datasets, performing lookups, and various other tasks essential for working with Census data efficiently.

## Files

### `input_output.py`
This is our file handling. It does the importing of csv, the export of csv, and custom file naming.

### `lookups.py`
This file handles the various lookups amongst the census data. It can doo lookups of widened/un-widened, consolidated or unconsolidated. It defaults to looking up by census code and geoname.

### `main.py`
Main method where all code should be run.

### `pdf.py`
The layout, format, and creation of pdfs is done here. It requires a logo image file, and input data to generate.

### `user_interface.py`
Experimental feature set. A work in progress to bring all lookup functions into a nice user interface. Needs further implementing.

### `validators.py`
This file contains the functions which handle user input validation, for a more stable usage.

### `visuals.py`
This file is to contain all code related to visual outputs, such as tables.

### `wrangling.py`
All functions related to data wrangling will be stored here. Functions include those that replace columns, shift data, calculate percentages, and flatten data. The functions here are used for both data cleaning and with data lookups.

## Sample Usages

### loading a file:
``` activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_TOTAL_WIDENED.csv', 2, 0) ```

### exporting a file:
```
file_exporter(df_list[0], 'a.csv')
```

### creating a pdf and using the auto file namer:
```
create_pdf(activeFile,'pdfs/'+file_namer(activeFile,2))
```

### wrangling csv's from original, to end goal:
```
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
activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1WC_TOTAL.csv', 2, 0)

activeFile = add_shifted_column(activeFile,5,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,5,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,8,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,8,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,11,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,11,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,14,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,14,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,17,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,17,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,20,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,20,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,23,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,23,"Female ",2, 0)

activeFile = add_shifted_column(activeFile,26,"Male ",1, 0)
activeFile = add_shifted_column(activeFile,26,"Female ",2, 0)

activeFile = specified_remove(activeFile,3,'Male %')
activeFile = specified_remove(activeFile,3,'Female %')

activeFile = column_row_delete(activeFile, 3, 1)

file_exporter(activeFile,'spreadsheets/FINAL/FINAL_EEOALL1WC_TOTAL_WIDENED.csv')
```

### loading a csv, doing a lookup, and exporting all results:
```
activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_TOTAL_WIDENED.csv', 2, 0)

df_list = ym_custom_area_builder(activeFile, -2, 2)

file_exporter(df_list[0], 'spreadsheets/custom/raw_'+file_namer(df_list[0], 1))
file_exporter(df_list[1], 'spreadsheets/custom/flattened_'+file_namer(df_list[1], 1))
file_exporter(df_list[2], 'spreadsheets/custom/percentages_'+file_namer(df_list[2], 1))

create_pdf(df_list[2], 'pdfs/'+file_namer(df_list[2], 2))
```
