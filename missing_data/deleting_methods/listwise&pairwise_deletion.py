
import pandas as pd

data = pd.read_csv() 
dataFrame = pd.DataFrame()

# LISTWISE DELETION
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna: 
# DataFrame.dropna(*, axis=0, how=_NoDefault.no_default, thresh=_NoDefault.no_default, 
# subset=None, inplace=False, ignore_index=False)

dataFrameCleaned = pd.dropna()

# PAIRWISE DELETION.
dataFrameCleanedPairwise = pd.dropna(subset=[row1, row2])