import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
egg_received = []
egg_released = []

with open('egg_data.csv') as csvfile:
	reader = csv.reader(csvfile)


name_list = ['2014','2015','2016','2017','2018']
num_list = [100000,150000,100000,50000,150000]
num_list1 = [80000,120000,90000,40000,140000]
x =list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
 
plt.bar(x, num_list, width=width, label='egg received',color='red')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='egg released',tick_label = name_list,color='orange')
plt.title("Rainbow Trout egg received&released")
plt.legend()
plt.show()

