import pickle

import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

housing = pd.DataFrame(pd.read_csv("Housing.csv"))
housing['price'] = np.log1p(housing['price'])

# Outlier Treatment
Q1 = housing.area.quantile(0.25)
Q3 = housing.area.quantile(0.75)
IQR = Q3 - Q1
housing = housing[(housing.area >= Q1 - 1.5 * IQR) & (housing.area <= Q3 + 1.5 * IQR)]

varlist = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']


# Defining the map function
def binary_map(x):
    return x.map({'yes': 1, "no": 0})


# Applying the function to the housing list
housing[varlist] = housing[varlist].apply(binary_map)

status = pd.get_dummies(housing['furnishingstatus'], drop_first=True)
housing = pd.concat([housing, status], axis=1)
housing.drop(['furnishingstatus'], axis=1, inplace=True)

df_train, df_test = train_test_split(housing, train_size=0.8, test_size=0.2, random_state=100)

y_train = df_train.pop('price')
y_test = df_test.pop('price')

dv = DictVectorizer(sparse=True)
train_dicts = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)

test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

mse = mean_squared_error(y_pred, y_test)
rmse = mean_squared_error(y_pred, y_test, squared=False)
r2 = r2_score(y_pred, y_test)
print('Mean Square Error(MSE):', mse)
print('Root Mean Square Error(RMSE):', rmse)
print('R2 score:', r2)

output_file = 'model.bin'
with open(output_file, 'wb') as f_out:
    pickle.dump((dv,lin_reg), f_out)
