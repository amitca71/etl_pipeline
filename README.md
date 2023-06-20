# etl_pipeline
Basic modular ETL pipeline 
the system decouples pipeline from implementation, in a way that allows modularity of each of the steps, as following:  

### extract -> transformation (one or more) -> loads (one or more)
each implementation is suplementad by its rellevant parameters from the parameter configuration file.
### main files and folders:
#### etl.py - the pipeline main
  the module is orchestrating the etl
  it reads the configuration file, and executes the run method of the implementation with its preconfigured set of parametes 
  and pandas datafreame from previos stage (except for extract, that provides the 1st dataframe)

#### config/parameters.json 
configurtion file that contains the parameters for implementation
each implementation contains the implementation name and parameters to be used
the configuration describes the following steps:
-  extract source
-  lists of transformation implementations
-  list of loads
sample content:
 {
     "extract": '{"impl_name":"csv_extract", "table_name": "usage"}',
     "transform": '[{"impl_name":"filter_out", "field":"status" , "value": "error"},\
                    {"impl_name":"aggregate", "dimension":"user_id" , "aggregate_column": "amount"}]',
     "loads": '[{"impl_name":"csv_output", "output_file_path": "/tmp/success_aggregated_by_user_id.csv"}]'

 }  
above implementaion would perform the follwoing steps:
#### current implelementation steps:
1. read csv files from: data/usage
2. filter out errored records
3. aggregats amount group by user_id
4. write the data to file: /tmp/success_aggregated_by_user_id.csv
   
#### implementations - root folder for the different implementations, with sub folders:
  the implementation file dscribed below are basic implementations that can easily be replaced 
  by others, and be called according to different configuration
  extract- contains the implementations for extracts 
        csv_extract.py - implementation for reding csv files from pre defined directory 
  transform- 
         filter_out.py - implementation of filter out records with column that contains specific value (according to configuration)
         aggregate.py - implementation of sum of numeric column group by dimension column        
  loads - 
         csv_output.py - implementation of loading output data to csv file, according to file name configuration
#### data (folder)
   used as an input source for demonstration purposes 
   folder structure is data/\<table-name\>/file (e.g. data/input/usage/      
                                                                     2023-06-18.csv  
                                                                     2023-06-19.csv)  

#### other files: 
etl_helper.py - implements generic methods, that can be used by other modules

## Instructions:
#### pre requisite:
i. python 3.7 +  
ii. virtualenv (pip install virtualenv)
#### installation:
1. clone the repository (git clone https://github.com/amitca71/etl_pipeline.git)
2. cd etl_pipeline
3. python -m venv .
4. . ./bin/activate
5. pip install -r requirements.txt
#### Execution (full etl exacution according to configuration and implementations): 
python etl.py 

