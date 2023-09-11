# importing module
from pandas import *
import matplotlib.pyplot as plt

## reading CSV file
data = read_csv("AI_test.csv")

## Convert  column data to list
ch1_data = data['ch1'].tolist()

## Plot
plt.xlabel('Points')
plt.ylabel('Voltage(V)')
plt.plot(ch1_data,  marker="o", markersize=3, markeredgecolor="red", markerfacecolor="green")
plt.show()