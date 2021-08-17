import numpy as np
import sklearn as sk
import matplotlib as mpl
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from random import random




#create time-series modelling - across different methodologies
def recursive_forecast(model, input_data, num_future_points):
    for point in range(num_future_points):
        prediction = model.predict(input_data)
        input_data = np.hstack((input_data, prediction))
    return prediction

#autoregression Model
def auto_regulation(x):
    data = [x + random() for x in range(1,100)]
    #fit model
    model = AutoReg(data, lags = 1)
    model_fit = model.fit()
    yhat = model_fit.predict(len(data), len(data))
    return yhat