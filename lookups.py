import prettytable as pt
import pandas as pd
from validators import *
from visuals import print_table
from wrangling import sum_and_flatten
from wrangling import df_to_percentages
from wrangling import apply_weights


def cc_lookup(df, cc_column):
    # ONLY FOR NOT WIDENED DATA SETS!

    """
    This function allows a user to find out about a specific job's employment data from its census code. When given a census job code, the function will report some percentages and amounts pertaining to that particular job.

    :param df: input data frame, typically the census data
    :param cc_column: (input) index of the Census Code column
    :input cc: int representing Census Code to look up
    :return: none
    """
    # input validation
    valid_codes = df.iloc[:, cc_column].tolist()
    cc = validate_int_list(valid_codes, "Census Code")

    result = df[df.iloc[:, cc_column] == cc]
    print(result.iloc[0, 13], ":")

    total_row = result.loc[result[result.columns[3]] == 'Total']
    total_num = total_row.iloc[0, 4]

    male_row = result.loc[result[result.columns[3]] == 'Male']
    male_num = male_row.iloc[0, 4]
    female_row = result.loc[result[result.columns[3]] == 'Female']
    female_num = female_row.iloc[0, 4]
    total_gender = male_num + female_num

    hispanic_num = total_row.iloc[0, 5]
    white_num = total_row.iloc[0, 6]
    black_num = total_row.iloc[0, 7]
    a_indian_num = total_row.iloc[0, 8]
    asian_num = total_row.iloc[0, 9]
    hawaiian_num = total_row.iloc[0, 10]
    two_or_more_num = total_row.iloc[0, 11]

    minority_num = hispanic_num + black_num + a_indian_num + asian_num + hawaiian_num + two_or_more_num
    total_race = minority_num + white_num

    female_percent = (female_num / total_gender) * 100
    minority_percent = (minority_num / total_race) * 100

    table = pt.PrettyTable()
    table.field_names = ("% Female", "% Minority", "Total", "Males", "Females", "White", "Minorities")
    table.add_row(
        [f"{female_percent:.1f}", f"{minority_percent:.1f}", f"{total_num:,}", f"{male_num:,}", f"{female_num:,}",
         f"{white_num:,}", f"{minority_num:,}"])

    print(table)


def cc_geo_lookup(df, cc_column, geo_column):
    # ONLY FOR NOT WIDENED DATA SETS!

    """
    This function is a modification of the original cc_lookup. It works in a similar manner, except it also allows the user to specify a location in the search.

    :param df: input data frame, typically the census data
    :param cc_column: (input) index of the Census Code column
    :param geo_column: (input) index of the GEONAME column to use
    :input cc: int representing Census Code to look up
    :input geo: string representing GEONAME Code to look up

    :return: none
    """
    # input validation
    valid_codes = df.iloc[:, cc_column].tolist()
    cc = validate_int_list(valid_codes, "Census Code")

    valid_geos = df.iloc[:, geo_column].tolist()
    geo = validate_string(valid_geos, "GEONAME")

    result = df[df.iloc[:, cc_column] == cc]
    result = result[result.iloc[:, geo_column] == geo]
    print(result.iloc[0, 2], " | ", result.iloc[0, 13], ":")

    total_row = result.loc[result[result.columns[3]] == 'Total']
    total_num = total_row.iloc[0, 4]

    male_row = result.loc[result[result.columns[3]] == 'Male']
    male_num = male_row.iloc[0, 4]
    female_row = result.loc[result[result.columns[3]] == 'Female']
    female_num = female_row.iloc[0, 4]
    total_gender = male_num + female_num

    hispanic_num = total_row.iloc[0, 5]
    white_num = total_row.iloc[0, 6]
    black_num = total_row.iloc[0, 7]
    a_indian_num = total_row.iloc[0, 8]
    asian_num = total_row.iloc[0, 9]
    hawaiian_num = total_row.iloc[0, 10]
    two_or_more_num = total_row.iloc[0, 11]

    minority_num = hispanic_num + black_num + a_indian_num + asian_num + hawaiian_num + two_or_more_num
    total_race = minority_num + white_num

    female_percent = (female_num / total_gender) * 100
    minority_percent = (minority_num / total_race) * 100

    table = pt.PrettyTable()
    table.field_names = ("% Female", "% Minority", "Total", "Males", "Females", "White", "Minorities")
    table.add_row(
        [f"{female_percent:.1f}", f"{minority_percent:.1f}", f"{total_num:,}", f"{male_num:,}", f"{female_num:,}",
         f"{white_num:,}", f"{minority_num:,}"])

    print(table)


def cc_geo_lookup_c(df, cc_column, geo_column):
    # ONLY FOR NOT WIDENED DATA SETS!
    """
    This function is a modification of the original cc_lookup. It works in a similar manner, except it also allows the user to specify a location in the search. This variant uses the consolidated

    :param df: input data frame, typically the census data
    :param cc_column: (input) index of the Census Code column
    :param geo_column: (input) index of the GEONAME column to use
    :input cc: int representing Census Code to look up
    :input geo: string representing GEONAME Code to look up

    :return: none
    """
    # input validation
    valid_codes = df.iloc[:, cc_column].tolist()
    cc = validate_int_list(valid_codes, "Census Code")

    valid_geos = df.iloc[:, geo_column].tolist()
    geo = validate_string(valid_geos, "GEONAME")

    result = df[df.iloc[:, cc_column] == cc]
    result = result[result.iloc[:, geo_column] == geo]
    print(result.iloc[0, 2], " | ", result.iloc[0, 13], ":")
    df_displayed = result.iloc[:, 3:12]

    table = pt.PrettyTable()
    table.field_names = df_displayed.columns.tolist()
    for index, row in df_displayed.iterrows():
        table.add_row(row)
    print(table)


def custom_area_builder(df, cc_column, geo_column):
    df_list = []

    valid_codes = df.iloc[:, cc_column].tolist()
    cc = validate_int_list(valid_codes, "Census Code")
    df = df[df.iloc[:, cc_column] == cc]

    print("Enter how many GEONAMES to consolidate:")
    number_of_geos = validate_int_min(0)
    geo_list = list()
    valid_geos = df.iloc[:, geo_column].tolist()

    for i in range(number_of_geos):
        geo = validate_string(valid_geos, "GEONAME")
        print(geo)
        geo_list.append(geo)

    weight_list = validate_weights(geo_list)
    result_df = pd.DataFrame()

    for n in geo_list:
        filtered_df = df[df.iloc[:, geo_column] == n]
        result_df = result_df._append(filtered_df, ignore_index=True)

    if not weight_list:
        df_list.append(result_df)

    else:
        result_df = apply_weights(result_df, 3, 26, weight_list)
        df_list.append(result_df)

    flattened_df = sum_and_flatten(result_df, 3, 26, geo_list)

    df_list.append(flattened_df)
    percent_flattened_df = df_to_percentages(flattened_df, 3, 26)
    df_list.append(percent_flattened_df)

    print_table(result_df)
    print_table(flattened_df)
    print_table(percent_flattened_df)

    return df_list


def lookup_menu(active_file, c_active_file):
    # super simple menu
    while True:
        choice = input("Enter 1 for 1W Lookup | 2 for 1WC Lookup | Anything else to exit: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Exiting.")
            break

        if choice == 1:
            cc_geo_lookup(active_file, 12, 2)
        elif choice == 2:
            cc_geo_lookup_c(c_active_file, 12, 2)
        else:
            print("Exiting.")
            break
