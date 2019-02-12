import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
Komoka = []
OxBow = []
Dingman = []

with open('membership_data.csv') as csvfile:
	reader = csv.reader(csvfile)


list_komoka = [15, 14, 23]
list_oxbow = [10, 18, 12]
list_dingman = [13, 15, 14]
year_list = ['2016', '2017', '2018']
x = list(range(len(year_list)))
total_width, n = 0.8, 3
width = total_width / n
plt.bar(x, list_komoka, width=width, label='Komoka', fc='y')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, list_oxbow, width=width, label='OxBow', tick_label=year_list, fc='r')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, list_dingman, width=width, label='Dingman', fc='b')
plt.title("Electrofishing Data")
plt.legend()
plt.show()


