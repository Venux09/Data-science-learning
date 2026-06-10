from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import root_mean_squared_error


#loading the data set 
housing = pd.read_csv('housing.csv')


#2.creating a Stratified test set based on Income category 
housing['income_cat'] = pd.cut(housing['median_income'],bins = [0,1.5,3,4.5,6,np.inf],labels = [1,2,3,4,5])

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2, random_state=42)
for test_index , train_index in split.split(housing,housing['income_cat']):
    strat_train_set = housing.loc[train_index].drop('income_cat',axis = 1)
    strat_test_set = housing.loc[test_index].drop('income_cat',axis = 1)


# work on a copy of training data 
housing = strat_train_set.copy()


# 3 . Separate features and lables 
housing_labels = housing['median_house_value'].copy()
housing_features = housing.drop('median_house_value',axis = 1 )

#4. separate the numerical value and categorical value 

housing_num = housing.drop('ocean_proximity',axis = 1).columns.tolist()
housing_text = ['ocean_proximity']

#5. Pipelines 

#Numerical Piplines 

num_pipeline = Pipeline([
    ('Imputer', SimpleImputer(strategy = 'median')),
    ('scaler',StandardScaler())
])


# categorical pipeline 
cat_pipeline = Pipeline([
    ("onehot",OneHotEncoder(handle_unknown="ignore"))
])

# full pipeline 
full_pipeline = ColumnTransformer([
    ("num",num_pipeline,housing_num),
    ("cat",cat_pipeline,housing_text)
])

#6. Transform the data 

housing_prepared = full_pipeline.fit_transform(housing)

print(housing_prepared.shape)



#7. train the model 

#linear regression 
lin_reag = LinearRegression()
lin_reag.fit(housing_prepared,housing_labels)
line_pred = lin_reag.predict(housing_prepared)
line_rmse = root_mean_squared_error(housing_labels,line_pred)
print(f" The mean squared error of the line reg in {line_rmse}")


#8.Decision Tree
dec_reag = LinearRegression()
dec_reag.fit(housing_prepared,housing_labels)
dec_pred = dec_reag.predict(housing_prepared)
dec_rmse = root_mean_squared_error(housing_labels,dec_pred)
print(f" The mean squared error of the dec_reg in {dec_rmse}")


#9. NOW - Random forest 


randome_forest_reag = LinearRegression()
randome_forest_reag.fit(housing_prepared,housing_labels)
randome_forest_pred = randome_forest_reag.predict(housing_prepared)
randome_forest_rmse = root_mean_squared_error(housing_labels,randome_forest_pred)
print(f" The mean squared error of the random_forest_reg in {randome_forest_rmse}")