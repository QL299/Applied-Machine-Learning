#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:53:38 2019

@author: Queenie
"""

import pandas as pd
iris = pd.read_csv('iris.data', delimiter = ',',header=None)
print(iris)
iris1 = pd.read_csv('iris.data', delimiter = ',', usecols = [0,1,2,3],header=None)
d = iris1.values.tolist()
d1 = d[:-1]
print (d1)
iris2 = pd.read_csv('iris.data', delimiter = ',',usecols = [4], header = None)
data = iris2.values.tolist()
data1 = data[:-1]
print(data1)



import seaborn as sns
import matplotlib.pyplot as plt
plt.figure()
sns.scatterplot(x=iris[0], y = iris[1], hue = iris[4])
plt.xlabel('sepal length in cm')
plt.ylabel('sepal width in cm')
plt.savefig("plot1.png")

plt.figure()
sns.scatterplot(x=iris[0], y = iris[2], hue = iris[4])
plt.xlabel('sepal length in cm')
plt.ylabel('petal length in cm')
plt.savefig("plot2.png")

plt.figure()
sns.scatterplot(x=iris[0], y = iris[3], hue = iris[4])
plt.xlabel('sepal length in cm')
plt.ylabel('petal width in cm')
plt.savefig("plot3.png")

plt.figure()
sns.scatterplot(x=iris[1], y = iris[2], hue = iris[4])
plt.xlabel('sepal width in cm')
plt.ylabel('petal length in cm')
plt.savefig("plot4.png")

plt.figure()
sns.scatterplot(x=iris[1], y = iris[3], hue = iris[4])
plt.xlabel('sepal width in cm')
plt.ylabel('petal width in cm')
plt.savefig("plot5.png")

plt.figure()
sns.scatterplot(x=iris[2], y = iris[3], hue = iris[4])
plt.xlabel('petal length in cm')
plt.ylabel('petal width in cm')
plt.savefig("plot6.png")


