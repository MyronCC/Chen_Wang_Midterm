import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
egg_received = []
egg_released = []

with open('egg_data.csv') as csvfile:
	reader = csv.reader(csvfile)


name_list = ['2014','2015','2016','2017','2018']
num_list = [100000,80000,70000,80000,100000]
num_list1 = [70000,70000,70000,70000,90000]
x =list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
 
plt.bar(x, num_list, width=width, label='egg received',color='green')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='egg released',tick_label = name_list,color='pink')
plt.title("Brown Trout egg received&released")
plt.legend()
plt.show()

