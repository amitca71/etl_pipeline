import pandas as pd
import etl_helper as eh
def run(parameter_dict):
    print(parameter_dict)
    input_root_dir="./data" if "input_root_dir" not in parameter_dict else parameter_dict['input_root_dir']
    directory=f"{input_root_dir}/input/{parameter_dict['table_name']}/"
    print(directory)
    return(eh.getAllDirData(directory))

