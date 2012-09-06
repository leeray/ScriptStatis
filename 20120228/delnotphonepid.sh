#!/bin/bash

while read line
do
	#echo $date1 $date2 $line
	#checkguid $date1 $date2 $line
	
	find ./TargetLog -name 'target-'$line'*' 
	find ./UVTargetLog -name 'target-'$line'*'

done < /home/lirui/otherpy/20120228/android_pid_notphone.log
		
	