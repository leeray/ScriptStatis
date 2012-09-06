#!/bin/bash



date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	
	day1=`date -d @$secdate1 +%Y/%m/%d`
	echo $day1

	secdate1=$(($secdate1 + 86400))
	
	cd /v2/LogTrees/init-statis/$day1
	
	pwd
	
	more nopid |grep '\(iPod touch;\|iPhone;\)'|grep '\^begin\^'| grep 'statis/vv' |awk -F '\\^_\\^' '{print $11}'|sort|uniq -c  > /v5/logs/20111214/$date1.log
	#more nopid |awk -F '\\^_\\^' '{print $3}'|grep '/openapi-wireless/videos/.*/playurl'|awk -F '\\/' '{print $4}'|sort|uniq -c > /v5/logs/20111214/$date1.log

done