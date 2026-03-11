# 1.Load Training and Testing data
# 2.Scale training data
# 3.Save scaled data into processed folder
import pickle 
from data_preprocessing import load_and_split_data
from sklearn.preprocessing import StandardScaler
import pandas as pd

x_train,x_test,y_train,y_test = load_and_split_data()

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

pd.DataFrame(x_train_scaled).to_csv("../data/processed/X_train.csv",index=False)
pd.DataFrame(x_test_scaled).to_csv("../data/processed/X_test.csv",index=False)
pd.DataFrame(y_train).to_csv("../data/processed/y_train.csv",index=False)
pd.DataFrame(y_test).to_csv("../data/processed/y_test.csv",index=False)

with open("../artifacts/scaler.pkl","wb") as f:
    pickle.dump(scaler,f)