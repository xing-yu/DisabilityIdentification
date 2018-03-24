# this scripts use pushshift to get comments of redditors

import requests
import os
import json
from datetime import datetime


#<<<<<<<<<<<<< name list >>>>>>>>>>>>>>

def nameList(files, paths):

	res = {}	# save the result

	# read names and labels into res
	# amputees and none amputees are store in 
	# separated files

	for i in range(len(files)):

		os.chdir(paths[i])

		f = open(files[i], 'r')

		for line in f:
			name = line.strip().split(",")[0]
			label = line.strip().split(",")[1]
			res[name] = label

		f.close()

	return res

#<<<<<<<<<<<<< get comments for a user >>>>>>>>>>>>

def getUserComments(user, file, beforeTimestamp):

	# url
	url = "https://apiv2.pushshift.io/reddit/search/comment/?author="
	url += user
	url += "&before="
	url += str(beforeTimestamp)
	url += "&limit=500"

	r = requests.get(url)

	# return if no data is received
	if r.status_code != 200:
		return None

	endTime = None

	for line in r.json()["data"]:
		json.dump(line, file)

		# update endstamp of this batch of comments
		timestamp = line["created_utc"]
		timestamp = datetime.fromtimestamp(int(timestamp))
		if endTime == None:
			endTime = timestamp
		else:
			if timestamp < endTime:
				endTime = timestamp

	if endTime != None:
		return int(endTime.timestamp())
	else:
		return None

#<<<<<<<<<<<< get comments >>>>>>>>>>>>>>>>>>>>>>

def getComments(users, path):

	# change to save path
	os.chdir(path)

	# save ending timestamp
	endTime = {}

	for user in users.keys():
		filename = user + ".txt"

		f = open(filename, 'a')

		timestamp = int(datetime.now().timestamp())

		# now curl the comments before the current timestamp

		while timestamp != None:
			endTime[user] = timestamp
			timestamp = getUserComments(user, f, timestamp)

		f.close()

	f = open("endTime.csv", "w")

	json.dump(endTime, f)

	f.close()


#<<<<<<<<<<<<<<<< main >>>>>>>>>>>>>>>>>>>>>>>>>>

usernamePath = "/Users/Xing/documents/IdentificationProject/Data_v2"

files = ["AmputeeNames.csv", "NonAmputeeNames.csv"]

paths = [usernamePath, usernamePath]

users = nameList(files, paths)

outputPath = "/Users/Xing/documents/IdentificationProject/Data_v3"

getComments(users, outputPath)




