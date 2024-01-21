import pandas as pd
from sklearn.linear_model import LinearRegression

# Other methods to read data: 
# read_clipboard(), read_excel(), read_feather(), read_feather()
# read_fwf(),read_hdf (), read_hdf (),read_hdf (),read_gbq (),read_html(),read_json (),
# read_orc (),read_parquet (),read_pickle (),read_sas (),read_spss (),read_sql ()
# read_sql_query (),read_sql_table (),read_stata (),read_table (),read_xml() 
data = pd.read_csv()
dataframe = pd.DataFrame(data)

def linearRegressionImputation(dataframe, targetVariable, predictorVariable):
    # to retain the original data, let's create a copy of the dataframe
    imputedDataframe = dataframe.copy()

    # create two sets of data, with and without the variable with 