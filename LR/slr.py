# y = b0 + b1x

"""

b1 = sum((xi - mean(x)*(yi - mean(y)))/sum((xi - mean(x))^2)

b0 = mean_Y - b1*mean_X

"""

import pandas as pd
import math
import numpy
import matplotlib.pyplot as plt


# Import Dataset
dataset = pd.read_csv('salary.csv')

# Seperate X and Y values
# iloc selects specific columns and rows from data
# : ka matlab get all rows
# [0] matlab get the 0th column
# flatten will convert 2d array to 1d array and tolist will convert it into a list
X = dataset.iloc[:,[0]].values.flatten().tolist()
Y = dataset.iloc[:,[1]].values.flatten().tolist()

mean_X = np.mean(X)
mean_Y = np.mean(Y)

b1_num = []
b1_denom = []


pred_y = []


# Upar wale formula ke hisaab se calculate the values for b0 and b1
for i in range(len(X)):
    b1_num.append((X[i] - mean_X)*(Y[i] - mean_Y))
    b1_denom.append(math.pow((X[i] - mean_X),2))
    
b1 = sum(b1_num)/sum(b1_denom)

b0 = mean_Y - b1*mean_X

# Calculate predicted values
for i in range(len(X)):
    pred_y.append(b0 + b1*X[i])
    
    
    
# Create a plot which plots your line
plt.scatter(X,Y)
plt.plot(X,pred_y, color='red')
plt.show()



   

