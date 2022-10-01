import csv
import json
from operator import index
from re import I
from unicodedata import name
from urllib import request
import pandas as pd
from sqlalchemy import create_engine

# def csvConvert(csv_path, json_path):

#     jsonData = {}

#     with open(csv_path, encoding='utf-8') as csvfile:
#         csvData = csv.DictReader(csvfile)
#         print(csvData)
#         for rows in csvData:
#             print(rows)
#             key = rows['No']
#             print(key)
#             jsonData[key] = rows

    

#     with open(json_path, 'w', encoding='utf-8') as jsonfile:
#         jsonfile.write(json.dumps(jsonData))

# csv_path = r'pythonCSV.csv'
# json_path = r'pythonJSON.json'

# csvConvert(csv_path, json_path)




engine = create_engine('postgresql+psycopg2://postgres:2003@localhost:5432/excel_database')
with pd.ExcelFile('Book.xlsx') as xls:
    df = pd.read_excel(xls)
    print(df)
    df.to_sql(name='first_table', con=engine, if_exists='append', index=False)



#read excel file

# db = pd.read_csv('pythonCSV.csv')

# print(db)


# # def PrintExcel(request):
#     file = request.POST.get('name')
#     i = pd.read_csv(file)
    
#     return 0
# fun = PrintExcel({'name':'Ali', 'yoshi':'28'})


