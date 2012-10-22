#!/bin/sh
#删除原始日志文件,先对比hadoop上是否有存储
#日志种类：api  go  ios  wap

argnum=$#
if [ $argnum -lt 3 ]; then
cat<<HELP
Usage: ./hadoop_log_check.sh ServerType date1 date2
ServerType:
    api go ios wap hash all
Example: 
    ./hadoop_log_check.sh api 20120101 20120105
HELP
    exit 1
fi

#参数定义
MOBILE="13911532419"

SourceLogType=$1
date1=$2
date2=$3

#邮件内容，每次运行前删除内容
mes_path="/home/lirui/Statis/hadoop_check/"
mes_file="hadoop_check_report.txt"

rm -f $mes_path$mes_file


#判断服务器类型
server_type=(api go ios wap hash all)
[[ "${server_type[@]/$1/}" == "${server_type[@]}" ]] && echo "$1 not in ServerType.\nServerType must be api|go|ios|wap|hash|all" && exit 1

#判断日期
datelen=${#date1}
STR_TEMP=`echo "$date1" | sed 's/[0-9]//g'`
if [ ! -z "$STR_TEMP" ]; then
    echo "sDate $date1 is not number or error"
    exit 1
fi
datelen=${#date2}
STR_TEMP=`echo "$date2" | sed 's/[0-9]//g'`
if [ ! -z "$STR_TEMP" ]; then
    echo "eDate $date2 is not number or error"
    exit 1
fi


function logfile_api_process () {
	file_date=$1
    
	hp_cmd="hadoop fs -dus /source/wireless/api/access/$file_date/*"
	$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=api_access -v file_date=$file_date -v OUTFILE=$mes_path$mes_file
	
	hp_cmd="hadoop fs -dus /source/wireless/api/statis/$file_date/*"
	$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=api_statis -v file_date=$file_date -v OUTFILE=$mes_path$mes_file

}

function logfile_ios_process () {
	file_date=$1
    
	hp_cmd="hadoop fs -dus /source/wireless/ios/access/$file_date/*"
	$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=ios -v file_date=$file_date -v OUTFILE=$mes_path$mes_file

}

function logfile_go_process () {
	file_date=$1
    
	hp_cmd="hadoop fs -dus /source/wireless/go/access/$file_date/*"
	$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=go -v file_date=$file_date -v OUTFILE=$mes_path$mes_file

}

function logfile_wap_process () {
	file_date=$1
    
	hp_cmd="hadoop fs -dus /source/wireless/wap/access/$file_date/*"
	$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=wap -v file_date=$file_date -v OUTFILE=$mes_path$mes_file

}

function logfile_hash_process () {
	file_date=$1
    hash_type=(api api2 go ios wap)
    for types in ${hash_type[@]}; do
        hp_cmd="hadoop fs -dus /source/wireless/hash/$types/$file_date/*"
        $hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=hash -v hashtype=$types -v file_date=$file_date -v OUTFILE=$mes_path$mes_file
    done;
	#hp_cmd="hadoop fs -dus /source/wireless/hash/$file_date/*"
	#$hp_cmd|awk -f hadoop_wireless_logcheck.awk -v server=hash -v file_date=$file_date -v OUTFILE=$mes_path$mes_file
	
}

#主程序开始
echo "$date1"
echo "$date2"
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
while [ "$secdate1" -le "$secdate2" ];do
	datestr=`date -d @$secdate1 +%Y%m%d`
	if [ $SourceLogType == "api" ];then
		logfile_api_process $datestr
	elif [ $SourceLogType == "go" ];then
		logfile_go_process $datestr
	elif [ $SourceLogType == "ios" ];then
		logfile_ios_process $datestr
	elif [ $SourceLogType == "wap" ];then
		logfile_wap_process $datestr
	elif [ $SourceLogType == "hash" ];then
		logfile_hash_process $datestr
	else
		logfile_api_process $datestr
		logfile_go_process $datestr
		logfile_ios_process $datestr
		logfile_wap_process $datestr
		logfile_hash_process $datestr
	fi;
	
	secdate1=$(($secdate1 + 86400))
done;


#mail -s "$date1 to $date2 hadoop checked report!" rui.li@youku.com yanhongkun@youku.com < $mes_path$mes_file

