# calculate average proportion of each bucket
# divided into two groups: amputees and none amputees
# plot the two groups
import os
import numpy as np

amputeeNameFile = "AmputeeNames.csv"
noneAmputeeNameFile = "NonAmputeeNames.csv"
datafile = "LIWC_bucketed.csv"
amputeesOut = "amputeeAvg.txt"
nonAmputeesOut = "nonAmputeeAvg.txt"
path = "/Users/Xing/Documents/IdentificationProject/Data_v3"

os.chdir(path)

#<<<<<<<<<<<<<<<<<<<<< read lables >>>>>>>>>>>>>>>>>>>
labels = {}

f = open(amputeeNameFile, 'r')

for line in f:
	data = line.strip().split(',')

	labels[data[0]] = 'A'

f.close()

f = open(noneAmputeeNameFile, 'r')

for line in f:
	data = line.strip().split(',')

	labels[data[0]] = 'N'

f.close()

#<<<<<<<<<<<<<<<<<<<<<<< average the buckets for amputees and nonamputees >>>>>>>>>>



f = open(datafile , 'r')

header = f.readline()

# store the matrices
amputees = {}
nonAmputees = {}

for line in f:
	data = line.strip().split(',')

	username = data[0].split('.')[0]

	values = data[1:]

	segment = int(values[0])

	if labels[username] == 'A':
		targetDict = amputees
	else:
		targetDict = nonAmputees

	if targetDict.get(segment) is None:
		targetDict[segment] = np.asarray(values).astype(np.float)
	else:
		targetDict[segment] = np.vstack((targetDict[segment], np.asarray(values).astype(np.float)))

f.close()

# write average value into output file

f = open(amputeesOut, 'w')

for key in amputees.keys():

	values = np.mean(amputees[key], axis = 0)

	f.write(','.join(map(str, list(values))))

	f.write('\n')

f.close()

f = open(nonAmputeesOut, 'w')

for key in nonAmputees.keys():

	values = np.mean(nonAmputees[key], axis = 0)

	f.write(','.join(map(str, list(values))))

	f.write('\n')

f.close()