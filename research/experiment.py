import os 
import pandas as pd
from sklearn.model_selection import train_test_split


wines = pd.read_csv("research/winequality-red.csv")

x = wines.drop(columns=["quality"],axis =1)
y = wines["quality"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import ElasticNet

lr = ElasticNet(alpha=0.1, l1_ratio=0.5, random_state=42)
lr.fit(x_train, y_train)
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
import numpy as np

def eval_metrics(actual, predicted):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return rmse, mae, r2

predicted_values = lr.predict(x_test)
rmse, mae, r2 = eval_metrics(y_test, predicted_values)
print("RMSE:", rmse)
print("MAE:", mae)
print("R2:", r2)