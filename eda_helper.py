import pandas as pd
import re as re
import os


# Helpful function to look through the columns of a dataframe
def eda_helper(df):
    dict_list = []
    for col in df.columns:
        data = df[col]
        dict_ = {}
        # The null count for a column. 
        dict_.update({"null_count" : data.isnull().sum()})
        # Counting the unique values in a column
        dict_.update({"unique_count" : len(data.unique())})
        # Finding the types of data in the column
        # This is useful for finding out potential problems with type mismatches
        dict_.update({"data_type" : set([type(d).__name__ for d in data])})
        #dict_.update({"score" : match[1]})
        dict_list.append(dict_)
    eda_df = pd.DataFrame(dict_list)
    eda_df.index = df.columns
    eda_df.sort_values(by=['null_count', 'unique_count'], ascending=[True, False], inplace=True)
        
    return eda_df



fileName = r"instr.csv"
fPath = r"/home/mitch/projects/proj_85_python_pandas_string_manipulation/"
filePath = os.path.join(fPath, fileName)

df = pd.read_csv(filePath)



var = eda_helper(df)
print(var)