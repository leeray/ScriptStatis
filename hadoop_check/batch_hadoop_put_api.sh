#!/bin/sh
START_DATE=$1
END_DATE=$2
COUNTER=0
CURRENT_DATE=$START_DATE

server_api=(142)

while [ $CURRENT_DATE -le $END_DATE ];do
    for ip in ${server_api[*]};do
        cmd="su shiwei -c \"hadoop fs -rm /home/shiwei/wireless/api/$CURRENT_DATE/"$CURRENT_DATE"_api_access_$ip.gz\""
        echo $cmd
        eval $cmd
        cmd="su shiwei -c \"hadoop fs -put /vol/logstat/wireless/api/"$CURRENT_DATE"_api_access_$ip.gz  /home/shiwei/wireless/api/$CURRENT_DATE/\""
        echo $cmd
        eval $cmd
        
        cmd="su shiwei -c \"hadoop fs -rm /home/shiwei/wireless/api/$CURRENT_DATE/"$CURRENT_DATE"_api_statis_$ip.gz\""
        echo $cmd
        eval $cmd
        cmd="su shiwei -c \"hadoop fs -put /vol/logstat/wireless/api/"$CURRENT_DATE"_api_statis_$ip.gz  /home/shiwei/wireless/api/$CURRENT_DATE/\""
        echo $cmd
        eval $cmd
    done;
    COUNTER=$(($COUNTER+1));
    CURRENT_DATE=$(date -d "$START_DATE +$COUNTER day" +%Y%m%d);
done;
