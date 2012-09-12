#!/usr/bin/awk -f 

BEGIN{
	com_200_0=0;
	com_100_0=0;
	com_101_0=0;
	com_102_0=0;
	com_104_0=0;
	com_105_0=0;
	com_106_0=0;
	com_999_0=0;
	com_400_0=0;
	com_403_0=0;
	com_0_0=0;
	com_othercode_0=0;
	com_nullcode_0=0;

	com_200_1=0;
	com_100_1=0;
	com_101_1=0;
	com_102_1=0;
	com_104_1=0;
	com_105_1=0;
	com_106_1=0;
	com_999_1=0;
	com_400_1=0;
	com_403_1=0;
	com_0_1=0;
	com_othercode_1=0;
	com_nullcode_1=0;
	
	com_xxx=0;
}
{
	if($18=="0"){
		if($5=="1"){
			com_200_0 += 1;
		}
		if($6=="1"){
			com_100_0 += 1;
		}
		if($7=="1"){
			com_101_0 += 1;
		}
		if($8=="1"){
			com_102_0 += 1;
		}
		if($9=="1"){
			com_104_0 += 1;
		}
		if($10=="1"){
			com_105_0 += 1;
		}
		if($11=="1"){
			com_106_0 += 1;
		}
		if($12=="1"){
			com_999_0 += 1;
		}
		if($13=="1"){
			com_400_0 += 1;
		}
		if($14=="1"){
			com_403_0 += 1;
		}
		if($15=="1"){
			com_0_0 += 1;
		}
		if($16=="1"){
			com_othercode_0 += 1;
		}
		if($17=="1"){
			com_nullcode_0 += 1;
		}
	}else if($18=="1"){
		if($5=="1"){
			com_200_1 += 1;
		}
		if($6=="1"){
			com_100_1 += 1;
		}
		if($7=="1"){
			com_101_1 += 1;
		}
		if($8=="1"){
			com_102_1 += 1;
		}
		if($9=="1"){
			com_104_1 += 1;
		}
		if($10=="1"){
			com_105_1 += 1;
		}
		if($11=="1"){
			com_106_1 += 1;
		}
		if($12=="1"){
			com_999_1 += 1;
		}
		if($13=="1"){
			com_400_1 += 1;
		}
		if($14=="1"){
			com_403_1 += 1;
		}
		if($15=="1"){
			com_0_1 += 1;
		}
		if($16=="1"){
			com_othercode_1 += 1;
		}
		if($17=="1"){
			com_nullcode_1 += 1;
		}
	}else{
		com_xxx += 1;
	}
}
END{
	print "200:", com_200_0, com_200_1;
	print "100:", com_100_0, com_100_1;
	print "101:", com_101_0, com_101_1;
	print "102:", com_102_0, com_102_1;
	print "104:", com_104_0, com_104_1;
	print "105:", com_105_0, com_105_1;
	print "106:", com_106_0, com_106_1;
	print "999:", com_999_0, com_999_1;
	print "400:", com_400_0, com_400_1;
	print "403:", com_403_0, com_403_1;
	print "0:", com_0_0, com_0_1;
	print "other:", com_othercode_0, com_othercode_1;
	print "null:", com_nullcode_0, com_nullcode_1;
	print "null_complete:", com_xxx

}
