import pandas as pd
import numpy as np


def set_pandas_frame_options():
    #pd.set_option("display.max_rows", 2)
    #pd.set_option("display.min_rows", 1)
    #pd.set_option('display.expand_frame_repr', False)
    pd.set_option("display.max.columns", 1000)
    #pd.set_option("display.precision", 2)

set_pandas_frame_options()


myDSF = pd.read_csv("datasets/drug-use-by-age-missing.csv")
#print(type(myDSF))
#print(len(myDSF))
#print(myDSF.shape)
#print(myDSF.head())
#print(myDSF.info())
#print(myDSF.describe())
myDSF.notna()
myDSF.interpolate()