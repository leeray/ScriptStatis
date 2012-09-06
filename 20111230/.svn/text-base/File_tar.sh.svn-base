#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@Tmp Log to File Tree@@@@@@@@@@@@@@@@@@@@@@@@@@@'
date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
dirtmp=$3
destdir=$4

echo $dirtmp
echo $destdir

function help(){
	echo "Parameter1: start time."
	echo "Parameter2: end time."
	echo "Parameter3: log source directory."
	echo "Parameter4: log tree destination directory."
	echo "Example:"
	echo "  sh File_tar.sh 20111001 20111002 /v4/tmplogs/ /v2/LogTrees/"
	return 0
}

if test -z $dirtmp -o $dirtmp = "./" -o $dirtmp = "/"
then
	echo " 3 argument error!"
	help
	exit 
fi

if test -z $destdir
then
	echo " 4 argument error!"
	help
	exit
fi


while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	
	if [ ! -e "$dirtmp/13" ]
	then
		mkdir $dirtmp/13
	fi
	if [ ! -e "$dirtmp/26" ]
	then
		mkdir $dirtmp/26
	fi
	
   	tar -zxf /v1/backuplogs/13/log.$date1.tar.gz -C $dirtmp/13/
   	tar -zxf /v1/backuplogs/26/log.$date1.tar.gz -C $dirtmp/26/
	
    /usr/local/bin/python /v5/logs/20111230/FileLog.py log.$date1 $dirtmp $destdir /v5/logs/LogTree/Log/

	rm -rf $dirtmp/13/log.$date1
	rm -rf $dirtmp/26/log.$date1


	secdate1=$(($secdate1 + 86400))

done
