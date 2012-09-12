#!/bin/sh

PROGRAM_PATH=/vol/users/xiazhiquan/Statis/20120903
HADOOP_PATH=$HADOOP_HOME

HADOOP_LOG_PATH='leeray/log'
HADOOP_HASH_PATH='/home/shiwei/wireless/hash'
HADOOP_RESULT_PATH='/tmp/xiazhiquan/leeray/statis'

date=$1
date_path=`date -d $date +%Y/%m/%d`

input_path="$HADOOP_HASH_PATH/$date/"
output_path="$HADOOP_RESULT_PATH/$date/"
echo $input_path ">>>" $output_path

cmd="$HADOOP_PATH/bin/hadoop fs -rmr $output_path"
echo $cmd
$cmd

cmd="$HADOOP_PATH/bin/hadoop jar $PROGRAM_PATH/statis.jar vvstatis $input_path $output_path"
echo $cmd
$cmd

cmd="$HADOOP_PATH/bin/hadoop fs -getmerge $HADOOP_RESULT_PATH/$date/ vv_statis_$date.log"
echo $cmd
$cmd

cmd="python $PROGRAM_PATH/vv_statis_merge.py $PROGRAM_PATH/vv_statis_$date.log $PROGRAM_PATH/vv_statis_"$date"_result.log"
echo $cmd
#$cmd

