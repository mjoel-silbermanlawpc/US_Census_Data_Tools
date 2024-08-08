from input_output import *
from lookups import *
from validators import *
from wrangling import *
from visuals import *
from user_interface import *
from pdf import *



activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_TOTAL_WIDENED.csv', 2, 0)
df_list = custom_area_builder(activeFile, -2, 2)
file_exporter(df_list[0], 'a.csv')
file_exporter(df_list[1], 'b.csv')
file_exporter(df_list[2], 'c.csv')

create_pdf(df_list[2],'pdfs/'+file_namer(df_list[2],2))

# file_exporter(df, file_namer(df,1))

'''
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
'''
# c_activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1WC_TOTAL.csv', 2, 0)
# lookup_menu(activeFile, c_activeFile)
