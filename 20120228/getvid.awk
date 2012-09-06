#!/usr/bin/awk -f 

# interface server access log hashfile
# 按pid、小时切分日志，注意系统ulimit 限制

# \/layout\/phone phone 接口
# \/openapi-cms\/ipad ipad首页
# (openapi-wireless)?\/(get|add|send|search|login|verifyUser|doRegister|hellotest|test) api 2.0 接口

# awk -f acccess_log.awk -v get="bbb=123&void=dfsa" -v post="abc=12321&safa=111" xxx.log



BEGIN{
    if(!get || !post) {
        print "error, noget nopost!";
        exit;
    }

    Time_begin = systime();

    print strftime("%Y-%m-%d %T",Time_begin) " Starting...";
}

{
	Param = $5'&'$6
	
	VID_offset = index(Param,"vid=");
	
	if (PID_offset == 0) {
		VID = "novid";
	}else{
		VID_START = substr(Param,PID_offset);
		
		VID_fenge1_offset = index(VID_START,"\"")
		VID_fenge2_offset = index(VID_START,"&")
		if (VID_fenge1_offset > VID_fenge2_offset){
		# '&'号先出现
			VID = substr(VID_START, 0, VID_fenge2_offset+1)
		}else{
		# '"'号先出现
			VID = substr(VID_START, 0, VID_fenge1_offset+1)
		}
	}

}

END{
	print VID
    if(Time_begin){
        Time_end = systime();
        print strftime("%Y-%m-%d %T",Time_end) " End";
        print "Take Time: " Time_end - Time_begin "s";
        print "Row Total: " NR "\n";
    }
}
