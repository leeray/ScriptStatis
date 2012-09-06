#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@Tmp Log to File Tree@@@@@@@@@@@@@@@@@@@@@@@@@'
function help(){
    echo "Parameter1: start time."
    echo "Parameter2: end time."
    echo "Parameter3: log tree directory."
	echo "Parameter4: log dir"
	echo "Example:"
    echo "  sh Stat_tree_android.sh 20111001 20111002 /v3/LogTrees/ /v5/log/LogTree/Log/"
    return 0
}


if [ "$1" = "--help" ]
then
        help
	exit
fi

if [ -z $1 ] || [ -z $2 ] || [ -z $3 ] || [ -z $4 ]
then
	echo "Invalid parameter!"
	help
	exit
fi

date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`

treedir=$3
logdir=$4
while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	/usr/local/bin/python /v5/logs/20111230/static_client_daily.py $treedir $date1 $logdir
	secdate1=$(($secdate1 + 86400))
done
