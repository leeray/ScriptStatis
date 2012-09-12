#!/bin/sh

#统计文件中 100 的 complete 为 0 和 1 的值分别有多少
#日志文件格式： $1pid-sessionid $2vv $3local $4playcode $5200 $6100 $7101 $8102 $9104 $10105 $11106 $12999 $13400 $14403 $150 $16othercode $17nullcode $18complete0 $19complete1 $20completeother $21completenull
#日志文件格式： $1pid-sessionid $2vv $3local $4playcode $5200 $6100 $7101 $8102 $9104 $10105 $11106 $12999 $13400 $14403 $150 $16othercode $17nullcode $18complete

date1=$1
secdate1=`date -d $date1 +%s`
file1=$2

tmp_file=/tmp/vv_complete_$date1.log

cmd="cat $file1|awk -f vv_complete_statis.awk"

echo $cmd
eval $cmd


