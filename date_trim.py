
import pandas as pd
import os

srcFolder = r"/home/mitch/projects/proj_85_python_pandas_string_manipulation/"
srcFile = f"date_trim.csv"
srcFile_ods = f"date_trim.ods"
srcPath = os.path.join(srcFolder, srcFile)

def date_trim(path='srcPath_csv'):
    df = pd.read_csv(srcPath)
    for each in df:
        print(len(each))
    return print(df)

#date_trim()



# 
a1 = '"*/2002-05-03/*"'
a2 = ''.join(i for i in a1 if i not in '"*/')
print(a2) 
