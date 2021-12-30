import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('eda_data.csv')

# choose relevant columns

df.columns

df_model=df[['Rating',Size]]
# get dummy data for categorical data
# create train, test split
# multiple linear regression
# lasso regression as data is gonna be sparse from the these dummy variables, so lasso helps in normalize that
# Random Forest

# Tune the model using GridSerachCV
# Test Ensembles