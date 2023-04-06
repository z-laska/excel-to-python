import pandas as pd
import sys


if len(sys.argv)!=3:
    print("Please provide paths to the excel file you want to convert and to the new json file as command line arguments.")
    sys.exit(1)

excel_filename = sys.argv[1]
json_filename = sys.argv[2]

try:
    data = pd.read_excel(excel_filename, sheet_name = 0)
except:
    print("An exception occured while reading your file.")
    print("Exiting program...")
    sys.exit(1)

whole_data = pd.DataFrame({"VersionInfo": "3.3.2.1902",  "EmployeeAbsences": [data]})
json_data = whole_data.to_json(path_or_buf = json_filename, orient="records", lines = True, indent=4)


