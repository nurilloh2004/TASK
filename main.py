import csv
import json
from operator import index
from unicodedata import name
import pandas as pd
from sqlalchemy import create_engine

def csvConvert(csv_path, json_path):

    jsonData = {}

    with open(csv_path, encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)

        for rows in csvData:
            key = rows['No']
            jsonData[key] = rows

    

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData))

csv_path = r'pythonCSV.csv'
json_path = r'pythonJSON.json'

csvConvert(csv_path, json_path)




engine = create_engine('postgresql+psycopg2://postgres:****@localhost:5432/excel_database')
with pd.ExcelFile('pythonCSV.xlsx') as xls:
    df = pd.read_excel(xls)
    df.ro_sql(name='first_table', con=engine, if_exists='append', index=False)

