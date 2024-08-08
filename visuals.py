import prettytable as pt
def print_table(df, mode=1):
    if mode == 1:
        excluded_columns = ["TBLID", "GEOID", "TITLE"]
        included_columns = [col for col in df.columns if col not in excluded_columns]

        table = pt.PrettyTable()
        table.field_names = included_columns

        for i in range(len(df)):
            table.add_row(df[included_columns].iloc[i].tolist())

        print(table)

    if mode == 2:
        print()
