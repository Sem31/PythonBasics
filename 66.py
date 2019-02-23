#  read excel files(.xlsx)


import pandas as pd 

dg  = pd.ExcelFile("Book.xlsx")
print(dg.sheet_names)

df = dg.parse("Sheet1")
print(df.head())