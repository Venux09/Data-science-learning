import os
import pandas as pd 
import numpy as np 
import joblib 
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
from sklearn.model_selection import cross_val_score


MODEL_FILE = 'model.pkl'
PIPELINE_FILE = 'pipeline.pkl'


def build_pipeline(housing_num,housing_text):
        
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
    return full_pipeline


if not os.path.exists(MODEL_FILE):
    #lets train the model j
        #loading the data set 
    housing = pd.read_csv('housing.csv') 

    #creating a Stratified test set based on Income category 
    housing['income_cat'] = pd.cut(housing['median_income'],bins = [0,1.5,3,4.5,6,np.inf],labels = [1,2,3,4,5])

    split = StratifiedShuffleSplit(n_splits=1,test_size=0.2, random_state=42)
    for train_index,test_index in split.split(housing,housing['income_cat']):
        
        housing.loc[test_index].drop('income_cat',axis = 1).to_csv('input.csv', index = False)
        housing = housing.loc[train_index].drop('income_cat',axis = 1)



    #Separate features and lables 
    housing_labels = housing['median_house_value'].copy()
    housing_features = housing.drop('median_house_value',axis = 1 )

    #attributes on the basis of number and their text
    housing_num = housing_features.drop('ocean_proximity',axis = 1).columns.tolist()
    housing_text = ['ocean_proximity']



    #buildings pipleline 
    pipeline = build_pipeline(housing_num , housing_text)
    housing_prepared = pipeline.fit_transform(housing_features)
    

    #model 
    model = RandomForestClassifier(random_state=42,   n_estimators=100, max_depth=12,             max_samples=0.8,      n_jobs=-1)
    model.fit(housing_prepared,housing_labels)

    #saving model and pipeline 

    joblib.dump(model,MODEL_FILE)
    joblib.dump(pipeline,PIPELINE_FILE)

    
else :
    #interference phase 
    model = joblib.load(MODEL_FILE)
    pipeline = joblib.load(PIPELINE_FILE)

    input_data = pd.read_csv('input.csv')
    transformed_input = pipeline.transform(input_data)
    predictions = model.predict(transformed_input)
    input_data['median_house_value'] = predictions

    input_data.to_csv('output.csv',index= False)
    print('inference is complete omoshoi desu ne ! to result saved in output.csv')
            



