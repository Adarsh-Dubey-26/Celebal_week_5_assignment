# -*- coding: utf-8 -*-
"""Celebal_weel_5_assignment.py

Original file is located at
    https://colab.research.google.com/drive/1LNc6EgseEWBCNQb7loZA510j_aK-XmaS

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""Importing the Boston House Price Dataset"""

house_price_dataset = sklearn.datasets.fetch_california_housing()

print(house_price_dataset)

house_price_dataframe = pd.DataFrame(house_price_dataset.data, columns = house_price_dataset.feature_names)

house_price_dataframe.head()

house_price_dataframe['price'] = house_price_dataset.target

house_price_dataframe.head()

house_price_dataframe.shape

house_price_dataframe.isnull().sum()

house_price_dataframe.describe()

"""Understanding the correlation between various features in the dataset

1. Positive Correlation

2. Negative Correlation
"""

correlation = house_price_dataframe.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

"""Splitting the data and Target"""

X = house_price_dataframe.drop(['price'], axis=1)
Y = house_price_dataframe['price']

print(X)
print(Y)

"""Splitting the data into Training data and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

XGBoost Regressor
"""

model = XGBRegressor()

model.fit(X_train, Y_train)

"""Evaluation

Prediction on training data
"""

training_data_prediction = model.predict(X_train)

print(training_data_prediction)

score_1 = metrics.r2_score(Y_train, training_data_prediction)

score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)

"""Visualizing the actual Prices and predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Price vs Preicted Price")
plt.show()

"""Prediction on Test Data"""

test_data_prediction = model.predict(X_test)

score_1 = metrics.r2_score(Y_test, test_data_prediction)

score_2 = metrics.mean_absolute_error(Y_test, test_data_prediction)

print("R squared error : ", score_1)
print('Mean Absolute Error : ', score_2)
