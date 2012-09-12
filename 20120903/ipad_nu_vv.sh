#!/bin/sh

#比较第一个和第二个文件， 将第二个文件中的文件拿出来，统计vv数据在 <0、0-3 、>3

date1=$1
secdate1=`date -d $date1 +%s`

nu_file0=$2
nu_file1=$3

tmp_file=/tmp/nu_vv_$date1.log

cmd="awk '{if(FILENAME==\"$nu_file0\")a[\$1]=1;else if(\$1 in a){print \$0}}' $nu_file0 $nu_file1"
echo $cmd
`eval $cmd > $tmp_file`

vv_0=0
vv_0_3=0
vv_3_6=0
vv_6_9=0
vv_9=0

#cmd="cat $tmp_file|awk '{if(\$3==0){vv_0=\$((vv_0+1))}else if(\$3>0 && \$3<=3){vv_0_3=$((vv_0_3+1))}else if(\$3>3 && \$3<=6){vv_3_6=$((vv_3_6+1))}else if(\$3>6 && \$3<=9){vv_6_9=$((vv_6_9+1))}else if(\$3>9){vv_9=$((vv_9+1))}else{echo \"aaaaaa\"}}'"

cmd="cat $tmp_file|awk 'BEGIN{vv_0=0;vv_0_3=0;vv_3_6=0;vv_6_9=0;vv_9=0;}{if(\$3==0){vv_0+=1}else if(\$3>0 && \$3<=3){vv_0_3+=1}else if(\$3>3 && \$3<=6){vv_3_6+=1}else if(\$3>6 && \$3<=9){vv_6_9+=1}else if(\$3>9){vv_9+=1}else{echo \"aaaaaa\"}}END{print vv_0, vv_0_3, vv_3_6, vv_6_9, vv_9}'"

echo $cmd
eval $cmd

echo $vv_0, $vv_0_3, $vv_3_6, $vv_6_9, $vv_9
