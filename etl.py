import importlib
import os
import etl_helper as eh
pipline_stage='extract'
extract_parameter_dict=eh.getDictFromLocalJsonFile(pipline_stage)
pkg = importlib.import_module(f"implementations.{pipline_stage}.{extract_parameter_dict['impl_name']}")
input_df=pkg.run(extract_parameter_dict)

pipline_stage='transform'
transform_parameter_list=eh.getDictFromLocalJsonFile(pipline_stage)
for transformation in transform_parameter_list:
    pkg = importlib.import_module(f"implementations.{pipline_stage}.{transformation['impl_name']}")
    input_df=pkg.run(input_df, transformation)

pipline_stage='loads'
load_parameter_list=eh.getDictFromLocalJsonFile(pipline_stage)
for load in load_parameter_list:
    pkg = importlib.import_module(f"implementations.{pipline_stage}.{load['impl_name']}")
    pkg.run(input_df, load)
