#creating data in python file 
import numpy as np 
import pandas as pd 

#random seed 
np.random.seed(42)



#number of rows of the data 
num_rows = 1000


#data generation 
data = {
    'Camera':np.random.randint(8,201,size=num_rows),
    'age':np.random.randint(0,4,size=num_rows),
    'ram':np.random.choice([4,5,8,12,16],size=num_rows),
    'cpu_score':np.random.randint(40,101,size=num_rows),
    'sd_slot':np.random.randint(0,2,size=num_rows),
    'sim':np.random.choice([1,2],size=num_rows),
    'price':np.random.randint(8000,70000,size=num_rows),

}

df = pd.DataFrame(data)

df.to_csv('Machine learning/Mobile_phones_data.csv',index =False)

print(df)
