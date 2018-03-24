#!/bin/bash

cd /Users/Xing/documents/IdentificationProject/Data_V3/comments
for file in *.txt;do
	jq -c '.' $file > temp01234.txt
	mv temp01234.txt /Users/Xing/documents/IdentificationProject/Data_V3/comments_2/$file
done