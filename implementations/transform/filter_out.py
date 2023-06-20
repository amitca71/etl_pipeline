def run(input_df, parameter_dict):
    return(input_df[input_df[parameter_dict['field']]!=parameter_dict['value']])

