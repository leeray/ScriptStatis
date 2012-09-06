#!/bin/bash

function checkguid(){
	secdate1=`date -d $1 +%s`
	secdate2=`date -d $2 +%s`

	while [ $secdate1 -le $secdate2 ]
	do
		
		while read line
		do
			#echo $date1 $date2 $line
			#checkguid $date1 $date2 $line
			
			date3=`date -d @$secdate1 +%Y%m%d`
		
			day1=`date -d @$secdate1 +%Y/%m/%d`
		
			
			echo /opt/data/log/$day1
			
			cat /opt/data/log/$day1/$line/statis_*|grep 'statis/vv'|grep 'type=begin' |awk -f '/home/lirui/otherpy/20120228/statis_parse_query_guid.awk'|sort|uniq -c  > /home/lirui/otherpy/20120228/UVSourceLog/$line-$date3.log
		
	
			/opt/python2.7/bin/python /home/lirui/otherpy/20120228/threadwork_uv.py $line-$date3.log target-$line-$date3.log
			
		done < /home/lirui/otherpy/20120228/android_pid.log
		
		secdate1=$(($secdate1 + 86400))
		
	done
	
}

date1=$1
date2=$2

checkguid $date1 $date2 $line

#while read line
#do
	#echo $date1 $date2 $line
	
#done < /home/lirui/otherpy/20120228/android_pid.log