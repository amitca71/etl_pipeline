def run(input_df, parameter_dict):
    return(input_df[[parameter_dict['dimension'],parameter_dict['aggregate_column'] ]].groupby(parameter_dict['dimension']).sum(parameter_dict['aggregate_column']))

