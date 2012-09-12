#!/bin/sh

PROGRAM_PATH=/vol/users/xiazhiquan/Statis/20120911
HADOOP_PATH=$HADOOP_HOME


HADOOP_LOG_PATH='leeray/log'
HADOOP_HASH_PATH='/home/shiwei/wireless/hash'
HADOOP_RESULT_PATH='/tmp/xiazhiquan/leeray/vv_complete_statis'

date=$1
date_path=`date -d $date +%Y/%m/%d`

input_path="$HADOOP_HASH_PATH/$date/"
output_path="$HADOOP_RESULT_PATH/$date/"
echo $input_path ">>>" $output_path

cmd="$HADOOP_PATH/bin/hadoop fs -rmr $output_path"
echo $cmd
$cmd

cmd="$HADOOP_PATH/bin/hadoop jar $PROGRAM_PATH/statis.jar vvStatisComplete $input_path $output_path"
echo $cmd
$cmd

cmd="$HADOOP_PATH/bin/hadoop fs -getmerge $HADOOP_RESULT_PATH/$date/ vv_complete_statis_$date.log"
echo $cmd
#$cmd


