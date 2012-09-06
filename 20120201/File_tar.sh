#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@Log to File Tree@@@@@@@@@@@@@@@@@@@@@@@@@@@'
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
	
	if [ ! -e "$dirtmp/25" ]
	then
		mkdir $dirtmp/25
	fi		
	if [ ! -e "$dirtmp/32" ]
	then
		mkdir $dirtmp/32
	fi		
	if [ ! -e "$dirtmp/33" ]
	then
		mkdir $dirtmp/33
	fi		
	if [ ! -e "$dirtmp/34" ]
	then
		mkdir $dirtmp/34
	fi
	if [ ! -e "$dirtmp/36" ]
	then
		mkdir $dirtmp/36
	fi		
	if [ ! -e "$dirtmp/37" ]
	then
		mkdir $dirtmp/37
	fi
	if [ ! -e "$dirtmp/71" ]
	then
		mkdir $dirtmp/71
	fi
	if [ ! -e "$dirtmp/72" ]
	then
		mkdir $dirtmp/72
	fi
	if [ ! -e "$dirtmp/25-statis" ]
    then
        mkdir $dirtmp/25-statis
	fi
	if [ ! -e "$dirtmp/32-statis" ]
	then
		mkdir $dirtmp/32-statis
	fi
	if [ ! -e "$dirtmp/33-statis" ]
	then
		mkdir $dirtmp/33-statis
	fi
	if [ ! -e "$dirtmp/34-statis" ]
	then
		mkdir $dirtmp/34-statis
	fi
	if [ ! -e "$dirtmp/36-statis" ]
	then
		mkdir $dirtmp/36-statis
	fi
	if [ ! -e "$dirtmp/37-statis" ]
	then
		mkdir $dirtmp/37-statis
	fi
	if [ ! -e "$dirtmp/71-statis" ]
	then
		mkdir $dirtmp/71-statis
	fi
	if [ ! -e "$dirtmp/72-statis" ]
	then
		mkdir $dirtmp/72-statis
	fi
	if [ ! -e "$dirtmp/13" ]
	then
		mkdir $dirtmp/13
	fi
	if [ ! -e "$dirtmp/26" ]
	then
		mkdir $dirtmp/26
	fi
	if [ ! -e "$dirtmp/16" ]
	then
		mkdir $dirtmp/16
	fi		
	if [ ! -e "$dirtmp/17" ]
	then
		mkdir $dirtmp/17
	fi		
	if [ ! -e "$dirtmp/12" ]
	then
		mkdir $dirtmp/12
	fi		
	if [ ! -e "$dirtmp/23" ]
	then
		mkdir $dirtmp/23
	fi		
	
	
	tar -zxf /v1/backuplogs/25/statis_log.$date1.tar.gz -C $dirtmp/25-statis/
	tar -zxf /v1/backuplogs/32/statis_log.$date1.tar.gz -C $dirtmp/32-statis/
	tar -zxf /v1/backuplogs/33/statis_log.$date1.tar.gz -C $dirtmp/33-statis/
	tar -zxf /v1/backuplogs/34/statis_log.$date1.tar.gz -C $dirtmp/34-statis/	
	tar -zxf /v1/backuplogs/36/statis_log.$date1.tar.gz -C $dirtmp/36-statis/	
	tar -zxf /v1/backuplogs/37/statis_log.$date1.tar.gz -C $dirtmp/37-statis/	
	tar -zxf /v1/backuplogs/71/statis_log.$date1.tar.gz -C $dirtmp/71-statis/	
	tar -zxf /v1/backuplogs/72/statis_log.$date1.tar.gz -C $dirtmp/72-statis/	
	tar -zxf /v1/backuplogs/25/access_log.$date1.tar.gz -C $dirtmp/25/
	tar -zxf /v1/backuplogs/32/access_log.$date1.tar.gz -C $dirtmp/32/
	tar -zxf /v1/backuplogs/33/access_log.$date1.tar.gz -C $dirtmp/33/
	tar -zxf /v1/backuplogs/34/access_log.$date1.tar.gz -C $dirtmp/34/
	tar -zxf /v1/backuplogs/36/access_log.$date1.tar.gz -C $dirtmp/36/
	tar -zxf /v1/backuplogs/37/access_log.$date1.tar.gz -C $dirtmp/37/
	tar -zxf /v1/backuplogs/71/access_log.$date1.tar.gz -C $dirtmp/71/
	tar -zxf /v1/backuplogs/72/access_log.$date1.tar.gz -C $dirtmp/72/
	tar -zxf /v1/backuplogs/16/log.$date1.tar.gz -C $dirtmp/16/
   	tar -zxf /v1/backuplogs/17/log.$date1.tar.gz -C $dirtmp/17/
   	tar -zxf /v1/backuplogs/13/log.$date1.tar.gz -C $dirtmp/13/
   	tar -zxf /v1/backuplogs/26/log.$date1.tar.gz -C $dirtmp/26/
	tar -zxf /v1/backuplogs/12/log.$date1.tar.gz -C $dirtmp/12/
    tar -zxf /v1/backuplogs/23/log.$date1.tar.gz -C $dirtmp/23/

	
	/usr/local/bin/python /v5/logs/20120201/FileLog.py log.$date1 $dirtmp $destdir /v5/logs/LogTree/Log/

	
	rm -rf $dirtmp/25/log.$date1
	rm -rf $dirtmp/32/log.$date1
	rm -rf $dirtmp/33/log.$date1
	rm -rf $dirtmp/34/log.$date1
	rm -rf $dirtmp/36/log.$date1
	rm -rf $dirtmp/37/log.$date1
	rm -rf $dirtmp/71/log.$date1
	rm -rf $dirtmp/72/log.$date1
	rm -rf $dirtmp/25-statis/log.$date1
	rm -rf $dirtmp/32-statis/log.$date1
	rm -rf $dirtmp/33-statis/log.$date1
	rm -rf $dirtmp/34-statis/log.$date1
	rm -rf $dirtmp/36-statis/log.$date1
	rm -rf $dirtmp/37-statis/log.$date1
	rm -rf $dirtmp/71-statis/log.$date1
	rm -rf $dirtmp/72-statis/log.$date1
    rm -rf $dirtmp/13/log.$date1
    rm -rf $dirtmp/26/log.$date1
	rm -rf $dirtmp/12/log.$date1
	rm -rf $dirtmp/23/log.$date1
	rm -rf $dirtmp/16/log.$date1
	rm -rf $dirtmp/17/log.$date1

	
	
	secdate1=$(($secdate1 + 86400))

done
