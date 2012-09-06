#! /bin/sh

logtreepath='/opt/Statis/otherpy/20120601'

if [ -d "$logtreepath" ];then
	mkdir -p $logtreepath
fi;

cd $logtreepath

date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
pid=$3

tmpfile=$pid'.tmp.log'
if [ -e "$logtreepath/$tmpfile" ];then
	rm -rf $logtreepath"/"$tmpfile
fi;

while [ $secdate1 -le $secdate2 ]
do
	date3=`date -d @$secdate1 +%Y%m%d`
	
	cmd="wget -q http://b24.hadoop.so.b28.youku:50075/streamFile?filename=/home/shiwei/wireless/hash/"$date3"/"$date3"_hash_go.tar.gz -O $date1.tar.gz"
	echo $cmd
	$cmd
	
	if [ -e "$logtreepath/$date1.tar.gz" ];then
		tar -xf $logtreepath/$date3.tar.gz
		
		for pid0 in `find ./ -name '$pid.api'`; do
			cat $pid0 >> $logtreepath"/"$tmpfile
		done;
			
        #cmd="rm -rf ./opt/*"
        #echo $cmd
        #$cmd
		
		rm -rf $logtreepath/$date3.tar.gz
	else
		echo "Error Not Found $date1.tar.gz"
	fi;
	
	secdate1=$(($secdate1 + 86400))
done

cat $logtreepath"/"$tmpfile | awk '{print $1}'|sort |uniq -e
