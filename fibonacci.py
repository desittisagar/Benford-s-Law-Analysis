from collections import Counter
import math
from scipy.stats import chisquare, chi2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fibb = [0 for x in range(0,501)]
fibb[1] = 1
fibb[2] = 1
#1. Fibonacci, 2. leading digits, 3. count, 4. percent(actual and benfords), 5. variation per digit, 6. chitest, 7. graph
def fibo(n):
	if n==1 or n==2:
		return fibb[1]

	elif fibb[n] != 0:
		return fibb[n]
	else:
		fibb[n] = fibo(n-1) + fibo(n-2)
		return fibb[n]


def leading_digits(list_):
	temp_lead = []
	for x in list_:
		i = x
		while(i >= 10):
			i = i // 10
		if x>0:
			temp_lead.append(i)
	return temp_lead


dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}


											#1
n = int(input("Enter a number for Fibonacci "))
#print(fibb)
fibo(n)

#print(fibb,"\n\n")

fibb1 = fibb
fibb1 = leading_digits(fibb1)		#2
#print("leading_digits", fibb1,"\n\n")


#dic = Counter(fibb1)				#3
for i in fibb1:
	if (i in dic):
		dic[i] += 1

sum=0.0
for i,k in dic.items():
	sum += k

actual_prediction = []

for i,k in dic.items():
	actual_prediction.append(((float)(k/sum)))

print("actual_prediction", actual_prediction,"\n\n")					#4


benfords_prediction = [.3010, .1761,.1249,.0969,.0792,.0669,.058,.0512,.0458]

print("benfords_prediction", benfords_prediction,"\n\n")

print("chi", chisquare(actual_prediction, benfords_prediction)[1],"\n\n")

variation_per_digit = []
sum1=0.0
for i,j in zip(actual_prediction, benfords_prediction):
	x = pow(i-j,2)/j
	sum1 += x
	variation_per_digit.append(x)

print("variation_per_digit", variation_per_digit,"\n\n")					#5

print(sum1,"\n\n")

#print("p-value", 1-chi2.cdf(x=sum1, df=8))

# 6 ChiTest---


#7 Graph plot


# x = [1,2,3,4,5,6,7,8,9]
# fig = plt.figure()
# ax1 = fig.add_subplot()
# ax1.set_xlabel('Fibonacci Comparison')
# ax1.plot(x, actual_prediction, 'b*-')
# ax1.tick_params(axis = 'y', labelcolor = 'b')
# ax1.set_ylabel('predicted', color = 'b')

# ax2 = ax1.twinx()
# ax2.plot(x, benfords_prediction, 'ro-')
# ax2.tick_params(axis = 'y', labelcolor = 'r')
# ax2.set_ylabel('expected', color = 'r')
# plt.show()


#for bar plot of Fibonacci

x_title = [str(x) for x in range(1,10)]
index = np.arange(9)
bar_width = 0.35
fig, ax = plt.subplots()
fibonnaci = ax.bar(index, actual_prediction, bar_width, label = 'Fibonacci')
benfords_prediction = ax.bar(index+bar_width, benfords_prediction, bar_width, label = 'benfords_prediction')
ax.set_xlabel("Category")
ax.set_ylabel("Digit Frequency")
ax.set_title("Actual vs Benfords Prediction")
ax.set_xticks(index+bar_width/2)
ax.set_xticklabels(x_title)
ax.legend()
plt.show()



df=pd.read_excel("Rivers1.xlsx")
df1=df[df.columns[2]]
df1.dropna(inplace=True)
l2=[]
for i in range(len(df1)):
    if "-" not in str(df1.iloc[i]):
        if "*" in str(df1.iloc[i]) and "(" not in str(df1.iloc[i]):
            x=df1.iloc[i].replace("*","").replace(",","")
            l2.append(x)
        elif "*" in str(df1.iloc[i]) and "(" in str(df1.iloc[i]):
            x=df1.iloc[i].replace("*","").replace(",","")
            l2.append(x[1:-1])
        elif " " in str(df1.iloc[i]):
            x=df1.iloc[i].replace(",","")
            y=str(df1.iloc[i]).index(" ")
            l2.append(x[0:y-1])
        
        else:
            l2.append(df1.iloc[i])
l2 = [int(i) for i in l2]
print("rivers ", l2)
l2.remove(4138)
print(len(l2))

# leading digits of l2

l2_lead_digits = leading_digits(l2)
print(l2_lead_digits)

# count dictionary
l2_dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for i in l2_lead_digits:
	if (i in l2_dic):
		l2_dic[i] += 1

print(l2_dic)

sum=0.0
for i,k in l2_dic.items():
	sum += k

l2_actual_prediction = []

for i,k in l2_dic.items():
	l2_actual_prediction.append(((float)(k/sum)))

print(l2_actual_prediction,"\n\n")
benfords_prediction = [.3010, .1761,.1249,.0969,.0792,.0669,.058,.0512,.0458]

print("benfords_prediction", benfords_prediction,"\n\n")

print("chi", chisquare(l2_actual_prediction, f_exp = benfords_prediction)[1],"\n\n")

variation_per_digit = []
sum1=0.0
for i,j in zip(l2_actual_prediction, benfords_prediction):
	x = pow(i-j,2)/j
	sum1 += x
	variation_per_digit.append(x)

print("variation_per_digit", variation_per_digit,"\n\n")					#5

print(sum1,"\n\n")	

# x = [1,2,3,4,5,6,7,8,9]
# fig = plt.figure()
# ax1 = fig.add_subplot()
# ax1.set_xlabel('Rivers in KM')
# ax1.plot(x, l2_actual_prediction, 'b*-')
# ax1.tick_params(axis = 'y', labelcolor = 'b')
# ax1.set_ylabel('predicted', color = 'b')

# ax2 = ax1.twinx()
# ax2.plot(x, benfords_prediction, 'ro-')
# ax2.tick_params(axis = 'y', labelcolor = 'r')
# ax2.set_ylabel('expected', color = 'r')
# plt.show()


#for bar plot of Rivers in Miles

x_title = [str(x) for x in range(1,10)]
index = np.arange(9)
bar_width = 0.35
fig, ax = plt.subplots()
rivers = ax.bar(index, l2_actual_prediction, bar_width, label = 'Rivers in KM')
benfords_prediction = ax.bar(index+bar_width, benfords_prediction, bar_width, label = 'benfords_prediction')
ax.set_xlabel("Category")
ax.set_ylabel("Digit Frequency")
ax.set_title("Actual vs Benfords Prediction")
ax.set_xticks(index+bar_width/2)
ax.set_xticklabels(x_title)
ax.legend()
plt.show()

#print(chi2.ppf(1.9955509623435634, df = 8))





import pandas as pd
import numpy as np
df=pd.read_excel("Rivers1.xlsx")
df1=df[df.columns[3]]
df1.dropna(inplace=True)
l2=[]
for i in range(len(df1)):
    if "-" not in str(df1.iloc[i]):
        if "*" in str(df1.iloc[i]) and "(" not in str(df1.iloc[i]):
            x=df1.iloc[i].replace("*","").replace(",","")
            l2.append(x)
        elif "*" in str(df1.iloc[i]) and "(" in str(df1.iloc[i]):
            x=df1.iloc[i].replace("*","").replace(",","")
            l2.append(x[1:-1])
        elif " " in str(df1.iloc[i]):
            x=df1.iloc[i].replace(",","")
            y=str(df1.iloc[i]).index(" ")
            l2.append(x[0:y-1])
        
        else:
            l2.append(df1.iloc[i])
l2 = [int(i) for i in l2]
print("rivers ", l2)
l2.remove(2571)
print(len(l2))

# leading digits of l2

l2_lead_digits = leading_digits(l2)
print(l2_lead_digits)

# count dictionary
l2_dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for i in l2_lead_digits:
	if (i in l2_dic):
		l2_dic[i] += 1

print(l2_dic)

sum=0.0
for i,k in l2_dic.items():
	sum += k

l2_actual_prediction = []

for i,k in l2_dic.items():
	l2_actual_prediction.append(((float)(k/sum)))

print(l2_actual_prediction,"\n\n")

benfords_prediction = [.3010, .1761,.1249,.0969,.0792,.0669,.058,.0512,.0458]

print("benfords_prediction", benfords_prediction,"\n\n")

print("chi", chisquare(l2_actual_prediction, f_exp = benfords_prediction)[1],"\n\n")

variation_per_digit = []
sum1=0.0
for i,j in zip(l2_actual_prediction, benfords_prediction):
	x = pow(i-j,2)/j
	sum1 += x
	variation_per_digit.append(x)

print("variation_per_digit", variation_per_digit,"\n\n")					#5

print(sum1,"\n\n")	

#for line plot of Rivers in Miles


# x = [1,2,3,4,5,6,7,8,9]
# fig = plt.figure()
# ax1 = fig.add_subplot()
# ax1.set_xlabel('Rivers in Miles')
# ax1.plot(x, l2_actual_prediction, 'b*-')
# ax1.tick_params(axis = 'y', labelcolor = 'b')
# ax1.set_ylabel('predicted', color = 'b')

# ax2 = ax1.twinx()
# ax2.plot(x, benfords_prediction, 'ro-')
# ax2.tick_params(axis = 'y', labelcolor = 'r')
# ax2.set_ylabel('expected', color = 'r')
# plt.show()


#for bar plot of Rivers in Miles

x_title = [str(x) for x in range(1,10)]
index = np.arange(9)
bar_width = 0.35
fig, ax = plt.subplots()
rivers = ax.bar(index, l2_actual_prediction, bar_width, label = 'Rivers in Miles')
benfords_prediction = ax.bar(index+bar_width, benfords_prediction, bar_width, label = 'benfords_prediction')
ax.set_xlabel("Category")
ax.set_ylabel("Digit Frequency")
ax.set_title("Actual vs Benfords Prediction")
ax.set_xticks(index+bar_width/2)
ax.set_xticklabels(x_title)
ax.legend()
plt.show()



# print(chisquare([8,9,7,8], f_exp = [8,8,8,8]))

# print(chisquare([.2916, .2083, .125, .0833, .0833, .0833, 0.0, .0833, .0416], f_exp = [.3010, .1761,.1249,.0969,.0792,.0669,.058,.0512,.0458]))