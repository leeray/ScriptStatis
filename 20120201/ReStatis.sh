#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@RESTATIS@@@@@@@@@@@@@@@@@@@@@@@@@@@'
date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	
	/usr/local/bin/python /v5/logs/20120201/DBclearData.py $date1
	
	sh /v5/logs/20120201/File_tar.sh $date1 $date1 /v4/tmplogs /v3/LogTrees/
	sh /v5/logs/20120201/Stat_tree_client.sh $date1 $date1 /v3/LogTrees/ /v5/logs/LogTree/Log/
	sh /v5/logs/20120201/DayToRun.sh $date1 $date1
	
	logdate=`date -d @$date1 +%Y/%m/%d`
	
	echo $logdate
	
	rm -rf /v3/LogTrees/$logdate/*

	secdate1=$(($secdate1 + 86400))

done
