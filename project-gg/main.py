from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer



#loading the data set 
housing = pd.read_csv('housing.csv')


#2.creating a Stratified test set based on Income category 
housing['income_cat'] = pd.cut(housing['median_income'],bins = [0,1.5,3,4,5,np.inf],labels = [1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2, random_state=42)
for test_index , train_index in split.split(housing,housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop('income_cat',axis = 1)
    strat_test_set = housing.loc[test_index].drop('income_cat',axis = 1)


# work on a copy of training data 
housing = strat_train_set.copy()


# 3 . Separate features and lables 
housing_labels = housing['median_house_value']
housing_features = housing.drop('median_house_value',axis = 1 )

#4. separate the numerical value and categorical value 

housing_num = housing.drop('ocean_proximity',axis = 1)
housing_text = housing['ocean_proximity']
print(housing_text)