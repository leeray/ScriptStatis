#!/usr/bin/awk -f 
BEGIN{
    if(!Outfile) {
        print "usage: awk -f statis_guid_tsv.awk -v Outfile=value file ...";
        exit;
    }

    Time_begin = systime();
    print strftime("%Y-%m-%d %T",Time_begin) " Starting...";
}

{
    parse_query($2,result);

    
    # 设备ID
    deviceid = result["deviceid"];
    
    # 用户唯一标识 guid
    guid = result["mac"]"&"result["imei"]"&"deviceid"&"result["uuid"];
    ##sh_md5 = "echo -n '"result["mac"]"&"result["imei"]"&"deviceid"&"result["uuid"]"' | md5sum | awk '{print $1}'"; 
    ##sh_md5 = "perl -MDigest::MD5=md5_hex -e'print md5_hex(\""result["mac"]"&"result["imei"]"&"deviceid"&"result["uuid"]"\")'";
    #sh_md5 | getline guid;
    #close(sh_md5);


    
    print "\""guid"\"" >> Outfile;
}

END{
    if(Time_begin){
        Time_end = systime();
        print strftime("%Y-%m-%d %T",Time_end) " End";
        print "Take Time: " Time_end - Time_begin "s";
        print "Row Total: " NR "\n";
    }
}

function parse_query(str,array) {
    delete array;
    split(str,arr,"&");
    for(i=1;i<=length(arr);i++) {
        split(arr[i],tmp,"=");
        if(length(tmp) > 2){
	        tmp_offset = index(arr[i],"=");
	        array[tmp[1]] = substr(arr[i],tmp_offset,length(arr[i]) - length(tmp[1]));
        }else{
            array[tmp[1]] = tmp[2];
        }
    }
}
