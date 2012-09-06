#!/bin/bash

num=0
while read brand
do
	num=$((num+1))
	echo $num
	#echo $brand
	file=$(ls)
	for grocery in $file  
	do
		#echo $grocery
		a=`awk -F "\\^_\\^" '$7 ~/'"$brand"'/' "$grocery"`
		#echo $a
		if [ "$a" = "" ]
		then 
			echo 'null'  $grocery '     ' $brand
		else 
			sed -i ''"$num"'s/$/, '"$grocery"'/' SonyEricsson
			echo '##############'
			#break
		fi
	done

done < SonyEricsson
