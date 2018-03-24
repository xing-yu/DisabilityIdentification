# break comments and posts into buckets
# based on time interval
# for example, Jhon's first comment is
# posted on Jan 01 2012 and last comment is
# on Aprl 03 2016.
# We can set buckets N = 10. All posts/comments are
# broken into files into 10 time intervals
# each interval is an file with corresponding 
# contents

import json
import glob
import os
from datetime import datetime
from datetime import timedelta

#<<<<<<<<<<<< get start time and end time of a user >>>>>>>>>>>>>>>>

# input a user file
# file start time, end time of the user's posting history
#
def startEnd(userFile):

	f = open(userFile, 'r')

	startTime = None
	endTime = None

	for line in f:

		data = json.loads(line)

		timestamp = int(data["created_utc"])

		time = datetime.fromtimestamp(timestamp)

		# update start and end time

		if startTime == None and endTime == None:
			startTime = time
			endTime = time
		else:
			if time < startTime:
				startTime = time

			if time > endTime:
				endTime = time

	f.close()

	return (startTime, endTime)

#<<<<<<<<<<<<< break JSON file >>>>>>>>>>>>>>>>>>>>>>>>>>

# input a JSON file, break it into separate JSON files 
# each include comments within a time interval

def breakJSONUniform(userFile, startTime, endTime, numberOfBuckets, outputDirectory):

	# bucket uniformly
	interval = (endTime - startTime)/numberOfBuckets

	boundary = endTime - interval

	f = open(userFile, 'r')
	fout = open(outputDirectory + userFile, 'w')

	for line in f:

		data = json.loads(line)

		timestamp = int(data["created_utc"])

		time = datetime.fromtimestamp(timestamp)

		# add segment symbol
		if time < boundary:
			boundary = boundary - interval
			fout.write("\n")
			fout.write("||Segment||")
			fout.write("\n")

			fout.write(str(data["body"]))

		# or just write output
		else:
			fout.write(str(data["body"]))

	f.close()
	fout.close()

#<<<<<<<<<<<<< break JSON file >>>>>>>>>>>>>>>>>>>>>>>>>>

# input a JSON file, break it into separate JSON files 
# each include comments within a time interval

def breakJSONByDays(userFile, startTime, endTime, numberOfDays, outputDirectory):

	interval = timedelta(30)

	boundary = startTime + interval

	f = reversed(list(open(userFile, 'r')))
	fout = open(outputDirectory + userFile, 'w')

	for line in f:

		data = json.loads(line)

		timestamp = int(data["created_utc"])

		time = datetime.fromtimestamp(timestamp)

		# add segment symbol
		if time > boundary:
			boundary = boundary + interval
			fout.write("\n")
			fout.write("||Segment||")
			fout.write("\n")

			fout.write(str(data["body"]))

		# or just write output
		else:
			fout.write(str(data["body"]))

	#f.close()
	fout.close()

#<<<<<<<<<<<<<<<<<<<<<<< main >>>>>>>>>>>>>>>>>>>>>>>>>


numberOfBuckets = 20
numberOfDays = 30
filepath = "/Users/Xing/documents/IdentificationProject/Data_v3/comments_lined"
#outputPath = "/Users/Xing/documents/IdentificationProject/Data_v3/comments_bucket/"
outputPath = "/Users/Xing/documents/IdentificationProject/Data_v3/comments_bucketByMonth/"

os.chdir(filepath)

time = {}

for filename in glob.glob('*.txt'):

	dates = startEnd(filename)

	# TODO: need to include post data, only comment data right now
	if dates[0] != None and dates[1] != None:

		time[filename.split('.')[0]] = startEnd(filename)
		#print(filename.split('.')[0] + ":" + str(time[filename.split('.')[0]]))

		#print(filename.split('.')[0], end = ": ")
		#diff = time[filename.split('.')[0]][1] - time[filename.split('.')[0]][0]
		#print(diff.days)
'''
for filename in glob.glob('*txt'):

	if time.get(filename.split('.')[0]):
		breakJSON(filename, time[filename.split('.')[0]][0], time[filename.split('.')[0]][1], numberOfBuckets, outputPath)

'''

for filename in glob.glob('*txt'):

	if time.get(filename.split('.')[0]):
		breakJSONByDays(filename, time[filename.split('.')[0]][0], time[filename.split('.')[0]][1], numberOfDays, outputPath)




	


