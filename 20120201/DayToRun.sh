#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@iPad Statis@@@@@@@@@@@@@@@@@@@@@@@@@@@'
date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	
	/usr/local/bin/python /v5/logs/20120201/iPadPvUvVv.py /v3/LogTrees/ $date1 /v5/logs/iPad/Log/
	/usr/local/bin/python /v5/logs/20120201/iPad214PvUvVv.py /v3/LogTrees/ $date1 /v5/logs/iPad/Log/
	
	secdate1=$(($secdate1 + 86400))

done
