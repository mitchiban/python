import pandas as pd
import os

fileName = r"instr.csv"
fPath = r"/home/mitch/projects/proj_85_python_pandas_string_manipulation/"
filePath = os.path.join(fPath, fileName)

def loaddf():
    df = pd.read_csv(filePath)
    return df

def findFileKey(df):

    for i in df.index:

        # Pattern n
            # loops through selected row value to determine if the pattern exists in that row?  (ie is the char position of pattern > 0)
            # if it does exist, will split file at char position and return the first index (ie left side)
            # if it does not exist, the original value will be used.

        pattern_1 = "<"
        pattern_2 = "??"
        pattern_3 = "_Y"

        if df.loc[i, 'file name'].find(pattern_1)> 0:
            df.loc[i,'file key'] = df.loc[i, 'file name'].split(pattern_1)[0]
 
        elif df.loc[i, 'file name'].find(pattern_2) > 0 :
            df.loc[i,'file key'] = df.loc[i, 'file name'].split(pattern_2)[0]
            
        elif df.loc[i, 'file name'].find(pattern_3) > 0 :
            df.loc[i,'file key'] = df.loc[i, 'file name'].split(pattern_3)[0]

        else:
            df.loc[i,'file key'] = df.loc[i, 'file name']
    
    print(df)
    return df

df = loaddf()
findFileKey(df)