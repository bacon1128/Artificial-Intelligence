import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error 

data_url = "https://raw.githubusercontent.com/hwweiCOAIPP/test/main/SimpleWeather.csv"

raw_df = pd.read_csv(data_url, sep=",", skiprows=2, header=None)

data = raw_df.values[:, 2:]
target = raw_df.values[:, 1]

train_data, test_data, train_target, test_target\
    =train_test_split(data, target, test_size=0.2, random_state=15)
print("HW2 408440450 林培瑋 ")
print(train_data.shape)
print(test_data.shape)

std_traindata = StandardScaler().fit_transform(train_data)
std_testdata = StandardScaler().fit_transform(test_data)
std_traintarget = StandardScaler().fit_transform(train_target.reshape(-1, 1))
std_testtarget = StandardScaler().fit_transform(test_target.reshape(-1, 1))
print(std_testtarget.shape)

LR = LinearRegression()
LR.fit(std_traindata, std_traintarget)
# evaluate the performance of your model
print("the value of default measurement of linear regression", LR.score(std_traindata, std_traintarget))

# predict the temperature
train_pred = LR.predict(std_traindata)
test_pred = LR.predict(std_testdata)


print("MSE train:%.3f, test:%.3f" %(mean_squared_error(std_traintarget, train_pred), mean_squared_error(std_testtarget, test_pred)))
