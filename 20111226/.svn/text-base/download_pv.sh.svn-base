#!/bin/sh

echo '@@@@@@@@@@@@@@@@@@@@Dwonload pv@@@@@@@@@@@@@@@@@@@@@@@@@@@'
date1=$1
date2=$2
secdate1=`date -d $date1 +%s`
secdate2=`date -d $date2 +%s`
dir=$3
destfile=$4

echo $dir

function help(){
    echo "Parameter1: start time."
	echo "Parameter2: end time."
    echo "Parameter3: source log directory."
    echo "Parameter4: statis reault file."
	echo "Example:"
    echo "  sh File_tar.sh 20111001 20111002 /v3/LogTrees/ ./20111226.cvs"
    return 0
}

if test -z $dir -o $dir = "./" -o $dir = "/"
then
	echo " 3 argument error!"
	help
	exit 
fi

if test -z $destfile -o $destfile = "./" -o $destfile = "/"
then
	echo " 4 argument error!"
	help
	exit 
fi

echo 'date, iphone_doc, ipad_doc, android_doc, apad_doc, android_sofe, apad_sofe, win7_sofe, wm_sofe, wid3_sofe, wid5_sofe, kjava_sofe, kjava_touchsofe, androidpaike, androidpaike_doc' > $destfile

while [ $secdate1 -le $secdate2 ]
do
	date1=`date -d @$secdate1 +%Y%m%d`
	echo $date1
	
	dir1=`date -d @$secdate1 +%Y/%m/%d`
	echo $day1
	
	iphone_doc=`more $dir/$dir1/nopid |grep /client/wp/%E4%BC%98%E9%85%B7iphone%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.0.doc|wc -l`
	ipad_doc=`more $dir/$dir1/nopid |grep /client/wp/%E4%BC%98%E9%85%B7ipad%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.1.3.doc|wc -l`
	android_doc=`more $dir/$dir1/nopid |grep /client/wp/%E4%BC%98%E9%85%B7Android%20phone%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E%20V2.0.docx|wc -l`
	apad_doc=`more $dir/$dir1/nopid |grep /client/wp/%E4%BC%98%E9%85%B7android%20pad%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8EV2.0.doc|wc -l`
	
	android_sofe=`more $dir/$dir1/nopid |grep /client/android/Youku_Phone_2.1_wangzhanxiazai.apk|wc -l`
	apad_sofe=`more $dir/$dir1/nopid |grep /client/android/Youku_aPad2.1_wangzhanxiazai.apk|wc -l`
	win7_sofe=`more $dir/$dir1/nopid |grep /client/wp/Youku.xap|wc -l`
	wm_sofe=`more $dir/$dir1/nopid |grep /client/wm/YouKu_v1.01.13.06007_Beta.CAB|wc -l`
	wid3_sofe=`more $dir/$dir1/nopid |grep /client/widget/Youku_type.wgz|wc -l`
	wid5_sofe=`more $dir/$dir1/nopid |grep /client/widget/Youku_touch.wgz|wc -l`
	kjava_sofe=`more $dir/$dir1/nopid |grep /client/java/Youku_type_beta.jar|wc -l`
	kjava_touchsofe=`more $dir/$dir1/nopid |grep /client/java/Youku_touch_beta.jar|wc -l`
	android_paike=`more $dir/$dir1/nopid |grep /client/android/Youku_Paike1.0.1_youkuguanwang_0112_2013.apk|wc -l`
	apaike_doc=`more $dir/$dir1/nopid |grep /client/android/%E4%BC%98%E9%85%B7%E6%8B%8D%E5%AE%A2%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BA%A7%E5%93%81%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E_V1.0.docx|wc -l`
	
	echo $date1, $iphone_doc, $ipad_doc, $android_doc, $apad_doc, $android_sofe, $apad_sofe, $win7_sofe, $wm_sofe, $wid3_sofe, $wid5_sofe, $kjava_sofe, $kjava_touchsofe, $android_paike, $apaike_doc >>  $destfile
	
	secdate1=$(($secdate1 + 86400))

done
