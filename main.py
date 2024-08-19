from input_output import *
from lookups import *
from validators import *
from wrangling import *
from visuals import *
from user_interface import *
from pdf import *

activeFile = file_loader('spreadsheets/FINAL/FINAL_EEOALL1W_TOTAL_WIDENED.csv', 2, 0)

df_list = ym_custom_area_builder(activeFile, -2, 2)

file_exporter(df_list[0], 'spreadsheets/custom/raw_'+file_namer(df_list[0], 1))
file_exporter(df_list[1], 'spreadsheets/custom/flattened_'+file_namer(df_list[1], 1))
file_exporter(df_list[2], 'spreadsheets/custom/percentages_'+file_namer(df_list[2], 1))

create_pdf(df_list[2], 'pdfs/'+file_namer(df_list[2], 2))
