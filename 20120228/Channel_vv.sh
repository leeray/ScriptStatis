#!/bin/bash

function checkpid(){
	secdate1=`date -d $1 +%s`
	secdate2=`date -d $2 +%s`

	while [ $secdate1 -le $secdate2 ]
	do
		date3=`date -d @$secdate1 +%Y%m%d`
		
		day1=`date -d @$secdate1 +%Y/%m/%d`
	
		secdate1=$(($secdate1 + 86400))
		
		echo /opt/data/log/$day1
		
		cat /opt/data/log/$day1/$3/statis_*|grep 'statis/vv'|grep 'type=begin' |awk -f '/home/lirui/otherpy/20120228/statis_parse_query.awk'|sort|uniq -c  > /home/lirui/otherpy/20120228/SourceLog/$3-$date3.log
	

		/opt/python2.7/bin/python /home/lirui/otherpy/20120228/threadwork.py $3-$date3.log target-$3-$date3.log
		
	done
	
}

date1=$1
date2=$2

while read line
do
	echo $date1 $date2 $line
	checkpid $date1 $date2 $line
done < /home/lirui/otherpy/20120228/android_pid.log