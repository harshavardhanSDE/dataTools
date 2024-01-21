import pandas as pd 

# Other methods to read data: 
# read_clipboard(), read_excel(), read_feather(), read_feather()
# read_fwf(),read_hdf (), read_hdf (),read_hdf (),read_gbq (),read_html(),read_json (),
# read_orc (),read_parquet (),read_pickle (),read_sas (),read_spss (),read_sql ()
# read_sql_query (),read_sql_table (),read_stata (),read_table (),read_xml() 
data = pd.read_csv()
dataframe = pd.DataFrame(data)

# Mean Imputation
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna
# DataFrame.fillna(value=None, *, method=None, axis=None, inplace=False, limit=None, 
# downcast=_NoDefault.no_default)
meanImputedValue = dataframe.fillna(dataframe.mean())

# The above method finds the missing value in the row, and replaces it with dataframe.mean(). 

# Median Imputation
medianImputeValue = dataframe.fillna(dataframe.median())
# Mode Imputation
modeImputedValue = dataframe.fillna(dataframe.mode())