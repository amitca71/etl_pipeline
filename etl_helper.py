import ast
import os
import fnmatch
import pandas as pd
def getDictFromLocalJsonFile( pipeline_stage, json_params_file='config/parameters.json'):
    with open(json_params_file) as conf_file:
        data = conf_file.read()
    file_as_dict = ast.literal_eval(data)
    return(ast.literal_eval(file_as_dict[pipeline_stage]))


def getAllDirData(directory, pattern="*.csv"):
    files = os.listdir(directory)
    print(files)
    list_pd=[]
    for file in files:

        if fnmatch.fnmatch(file, pattern):
                print(file)
                df=pd.read_csv(f'{directory}/{file}')
                list_pd.append(df)
    if (len(list_pd)==0):
            return None
    return(pd.concat(list_pd))