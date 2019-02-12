import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []
membership = []

with open('membership_data.csv') as csvfile:
	reader = csv.reader(csvfile)


name_list = ['2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
num_list = [52,48,67,45,45,50,55,67,65,70,60,60,55,60,65,75,80]
plt.figure(figsize=(12,4))
plt.plot(name_list,num_list,linewidth=2)
plt.title("Membership change")
plt.show()


