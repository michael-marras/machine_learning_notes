import numpy as np
import pandas as pd

myindex = ['USA', 'Canada', 'Mexico']
mydata = [1776, 1867, 1821]
myser = pd.Series(mydata, myindex) #First argument = data, Second argument = index/keys

ages = {'Sam':5, 'Frank':10, 'Spike': 7}
dictionary = pd.Series(ages) #creates indexed dictionary
print(dictionary)
print(myser)

q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

print(sales_q1['Japan'])

np.array([1,2]) * 2 #multiply each element of [1,2] by 2
print(sales_q1 /100)
print(sales_q1 + sales_q2)
print(sales_q1.add(sales_q2, fill_value = 0))
print(sales_q1.dtype)
first_half = sales_q1.add(sales_q2, fill_value = 0)
print(first_half.dtype)