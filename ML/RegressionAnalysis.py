import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split


housedata=pd.read_csv('kc_house_data.csv')
print(housedata.shape,housedata.columns)

house_df = housedata[['price','date','bedrooms','sqft_living',  'floors', 'waterfront', 'view', 'condition', 'grade','zipcode' ]]
print(house_df)


#split year and month from date considering price depends on year and month of sale
# bedrooms, bathrooms, floors, waterfront, view, condition, grade, year and month as categorical features

house_df['year']=housedata['date'].str[0:4]
house_df['month']=housedata['date'].str[4:6]
print(house_df)