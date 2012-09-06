#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@Dwonload pv@@@@@@@@@@@@@@@@@@@@@@@@@@@'
date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
wap=$3
destfile=$4

echo $wap

function help(){
	echo "Parameter1: start time."
	echo "Parameter2: end time."
	echo "Parameter3: source log directory."
	echo "Parameter4: statis reault file."
	echo "Example:"
	echo "  sh download_pv.sh 20120201 20120229 /opt/data/log/wap ./20111226.cvs"
	return 0
}

if test -s $date1 
then
	echo " 1 argument error!"
	help
	exit
fi

if test -s $date2
then
	echo " 2 argument error!"
	help
	exit
fi

if test -z "$wap" -o "$wap" = "./" -o "$wap" = "/"
then
	echo " 3 argument error!"
	help
	exit 
fi

if test -z "$destfile" -o "$destfile" = "./" -o "$destfile" = "/"
then
	echo " 4 argument error!"
	help
	exit 
fi

echo 'date, android_sofe, android_sofe_0227, android_sofe_2_2, apad_sofe, apad_soft_2_2, win7_sofe, wm_sofe, wid3_sofe, wid5_sofe, kjava_sofe, kjava_touchsofe, androidpaike1.0.1, androidpaike1.0.2, androidpaike1.0.2.2, androidpaike1.0.3, androidpaike1.3' > $destfile

while [ $secdate1 -le $secdate2 ]
do
	
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	date2=`date -d @$secdate1 +%Y/%m/%d`
	echo $date2
	
	cd $wap
	cmd="wget -q http://b24.hadoop.so.b28.youku:50075/streamFile?filename=/home/shiwei/wireless/hash/"$date1"/"$date1"_hash_wap.tar.gz -O $date1.tar.gz"
	echo $cmd
	$cmd
		
	if [ -e "$wap/$date1.tar.gz" ];then
		tar -zxf $wap/$date1.tar.gz
		
		#if [ ! -d "$wap/wap/$date2" ]
		#then
		#	mkdir -p $wap/wap/$date2
		#fi

		cmd="mv $wap/backup/hashback/wap/$date1 $wap/$date1"
		echo $cmd
		$cmd
		
		rm -f $wap/$date1.tar.gz
	else
		echo "Error Not Found $date1.tar.gz"
	fi;
	
	
	#文档
	#iphone_doc=`cat $wap/$date1 |grep /client/wp/%E4%BC%98%E9%85%B7iphone%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.0.doc|wc -l`
	#ipad_doc=`cat $wap/$date1 |grep /client/wp/%E4%BC%98%E9%85%B7ipad%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.1.3.doc|wc -l`
	#android_doc=`cat $wap/$date1 |grep /client/wp/%E4%BC%98%E9%85%B7Android%20phone%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%20V2.0.docx|wc -l`
	#apad_doc=`cat $wap/$date1 |grep /client/wp/%E4%BC%98%E9%85%B7android%20pad%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.0.doc|wc -l`
	#apaike_doc=`cat $wap/$date1 |grep /client/android/%E4%BC%98%E9%85%B7%E6%8B%8D%E5%AE%A2%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E_V1.0.docx|wc -l`
	
	#主客户端
	android_sofe=`cat $wap/$date1 |grep /client/android/Youku_Phone_2.1_wangzhanxiazai.apk|wc -l`
	android_sofe2027=`cat $wap/$date1 |grep /client/android/Youku_Phone_2.1.1_wangzhanxiazai_0227_1623.apk|wc -l`
	android_sofe_2_2=`cat $wap/$date1 |grep /client/android/Youku_Phone_2.2_Wangzhanxiazai_0423_1740.apk|wc -l`
	
	#主pad客户端
	apad_sofe=`cat $wap/$date1 |grep /client/android/Youku_aPad2.1_wangzhanxiazai.apk|wc -l`
	apad_soft_2_2=`cat $wap/$date1 |grep /client/android/Youku_pad_2.2_Wangzhanxiazai_0424_0950.apk|wc -l`
	
	#windows phone7版
	win7_sofe=`cat $wap/$date1 |grep /client/wp/Youku.xap|wc -l`
	#window mobile版
	wm_sofe=`cat $wap/$date1 |grep /client/wm/YouKu_v1.01.13.06007_Beta.CAB|wc -l`
	
	#Widget s60 3th(按键)版
	wid3_sofe=`cat $wap/$date1 |grep /client/widget/Youku_type.wgz|wc -l`
	#Widget s60 5th(触屏)版
	wid5_sofe=`cat $wap/$date1 |grep /client/widget/Youku_touch.wgz|wc -l`
	
	#Kjava(按键)版
	kjava_sofe=`cat $wap/$date1 |grep /client/java/Youku_type_beta.jar|wc -l`
	#Kjava(触屏)版
	kjava_touchsofe=`cat $wap/$date1 |grep /client/java/Youku_touch_beta.jar|wc -l`
	
	#android 拍客
	android_paike=`cat $wap/$date1 |grep /client/android/Youku_Paike1.0.1_youkuguanwang_0112_2013.apk|wc -l`
	android_paike1_2=`cat $wap/$date1 |grep /client/android/Youku_Paike1.0.2_youkuguanwang.apk|wc -l`
	android_paike1_2_2=`cat $wap/$date1 |grep /client/android/Youku_Paike1.0.2.2_mobile_youku_0227_1130.apk|wc -l`
	android_paike1_0_3=`cat $wap/$date1|grep /client/android/Youku_Paike1.0.3_mobile_youku_0313_1147.apk|wc -l` 
	android_paike1_3=`cat $wap/$date1|grep /client/android/Youku_Paike1.3_Web_0703_1037.apk|wc -l`
	
	#ipaike_doc=`cat $wap/$date1 |grep /client/iphone/%E4%BC%98%E9%85%B7%E6%8B%8D%E5%AE%A2%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8Eiphone%E7%89%88V1.0.pdf|wc -l`
	
	echo $date1, $android_sofe, $android_sofe2027, $android_sofe_2_2, $apad_sofe, $apad_soft_2_2, $win7_sofe, $wm_sofe, $wid3_sofe, $wid5_sofe, $kjava_sofe, $kjava_touchsofe, $android_paike, $android_paike1_2, $android_paike1_2_2 , $android_paike1_0_3 , $android_paike1_3 >>  $destfile
	
	rm -f $wap/$date1
	
	secdate1=$(($secdate1 + 86400))

done
