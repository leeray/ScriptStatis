BEGIN{
	h["api2.tar.gz"]=20;
	h["go.tar.gz"]=2;
	h["ios.tar.gz"]=2;
	h["wap.tar.gz"]=200;
	h["api.tar.gz"]=800;
	
	s["api"]=20;
	s["api2"]=2;
	s["go"]=2;
	s["ios"]=40;
	s["wap"]=200;
	
	filelength_api_access=180
	filelength_api_statis=30
	filelength_wap=200
	filelength_go=3
	filelength_ios=2
	
	server_api="25;32;33;34;36;37;38;39;40;71;72;142;73;74;75;77;78;79;80;86;87;88;89;90;161;162;163";
	split(server_api, arr_api, /;/);
	
	server_wap="13;26";
	split(server_wap, arr_wap, /;/);
	
	server_go="16;17";
	split(server_go, arr_go, /;/);
	
	server_ios="12;23";
	split(server_ios, arr_ios, /;/);
}
{
	url = $1;
	f_index = index(url, file_date"_");
	f_name = "";
	if(f_index==0){
		f_name = url;
	}else{
		f_name = substr(url, f_index);
	}
	hd[f_name]=$2;
}
END{
	if(server=="hash"){
		#for(sf in s){}
		#for(hf in h){
			a_filename = file_date"_hash_"hashtype".tar.gz";
			if(hd[a_filename] != ""){
				len_hd_filename = hd[a_filename] / 1024 / 1024;
				if(len_hd_filename < s[hashtype]){
					print "Server: Hash, Date: "file_date", File: "a_filename", The File is too small. "len_hd_filename"M < "s[hashtype]"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: Hash, Date: "file_date", File: "a_filename", Could not find the file." >> OUTFILE;
			}
		#}
	    #}
	}
	
	if(server=="api_access"){
		len_api = length(arr_api)
		for(i=1;i<=len_api;i++){
			if( (arr_api[i]=="36" || arr_api[i]=="37") && file_date < "20120120" ){
				continue
			}
			if( (arr_api[i]=="71" || arr_api[i]=="72") && file_date < "20120323" ){
				continue
			}
			if( (arr_api[i]=="38" || arr_api[i]=="39" || arr_api[i]=="40") && file_date < "20120712" ){
				continue
			}
			if( (arr_api[i]=="73" || arr_api[i]=="74" || arr_api[i]=="75") && file_date < "20120926" ){
				continue
			}
			if( arr_api[i]=="142" && file_date < "20120803" ){
				continue
			}
			if( (arr_api[i] ~ /77|78|79|80|86|87|88|89|90|161|162|163/) && file_data < "20121010" ){
				continue
			}
			
			a_filename_access = file_date"_api_access_"arr_api[i]".gz";
			if(hd[a_filename_access] != ""){
				len_hd_filename = hd[a_filename_access] / 1024 / 1024 ;
				if((arr_api[i]!="142" && len_hd_filename < filelength_api_access) || (arr_api[i]=="142" && len_hd_filename < 20)){
					print "Server: API, Date: "file_date", File: "a_filename_access", The File is too small. "len_hd_filename"M < "filelength_api_access"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: API, Date: "file_date", File: "a_filename_access", Could not find the file." >> OUTFILE;
			}
		}
	}
	
	if(server=="api_statis"){
		len_api = length(arr_api)
		for(i=1;i<=len_api;i++){
			if( (arr_api[i]=="36" || arr_api[i]=="37") && file_date < "20120120" ){
				continue
			}
			if( (arr_api[i]=="71" || arr_api[i]=="72") && file_date < "20120323" ){
				continue
			}
			if( (arr_api[i]=="38" || arr_api[i]=="39" || arr_api[i]=="40") && file_date < "20120712" ){
				continue
			}
			if( (arr_api[i]=="73" || arr_api[i]=="74" || arr_api[i]=="75") && file_date < "20120926" ){
				continue
			}
			if( arr_api[i]=="142" && file_date < "20120803" ){
				continue
			}
			if( (arr_api[i] ~ /77|78|79|80|86|87|88|89|90|161|162|163/) && file_data < "20121010" ){
				continue
			}
			
			a_filename_statis = file_date"_api_statis_"arr_api[i]".gz";
			if(hd[a_filename_statis] != ""){
				len_hd_filename = hd[a_filename_statis] / 1024 / 1024 ;
				if((arr_api[i]!="142" && len_hd_filename < filelength_api_statis) || (arr_api[i]=="142" && len_hd_filename < 4)){
					print "Server: API, Date: "file_date", File: "a_filename_statis", The File is too small. "len_hd_filename"M < "filelength_api_statis"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: API, Date: "file_date", File: "a_filename_statis", Could not find the file." >> OUTFILE;
			}
		}
	}
	
	if(server=="wap"){
		len_api = length(arr_wap)
		for(i=1;i<=len_api;i++){
			if(file_date < "20111228" && arr_wap[i]=="26"){
				continue
			}
			
			a_filename = file_date"_wap_access_"arr_wap[i]".gz";
			if(hd[a_filename] != ""){
				len_hd_filename = hd[a_filename] / 1024 / 1024;
				if(len_hd_filename < filelength_wap){
					print "Server: WAP, Date: "file_date", File: "a_filename", The File is too small. "len_hd_filename"M < "filelength_wap"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: WAP, Date: "file_date", File: "a_filename", Could not find the file." >> OUTFILE;
			}
		}
	}
	
	if(server=="go"){
		len_api = length(arr_go)
		for(i=1;i<=len_api;i++){
			a_filename = file_date"_go_access_"arr_go[i]".gz";
			if(hd[a_filename] != ""){
				len_hd_filename = hd[a_filename] / 1024 / 1024;
				if(len_hd_filename < filelength_go){
					print "Server: GO, Date: "file_date", File: "a_filename", The File is too small. "len_hd_filename"M < "filelength_go"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: GO, Date: "file_date", File: "a_filename", Could not find the file." >> OUTFILE;
			}
		}
	}
	
	if(server=="ios"){
		len_api = length(arr_ios)
		for(i=1;i<=len_api;i++){
			if(file_date > "20120223" && arr_ios[i]=="23"){
				continue
			}
			
			a_filename = file_date"_ios_access_"arr_ios[i]".gz";
			if(hd[a_filename] != ""){
				len_hd_filename = hd[a_filename] / 1024 / 1024;
				if(len_hd_filename < filelength_ios){
					print "Server: IOS, Date: "file_date", File: "a_filename", The File is too small. "len_hd_filename"M < "filelength_ios"M ." >> OUTFILE;
				}else{
					print a_filename" size:"len_hd_filename
				}
			}else{
				print "Server: IOS, Date: "file_date", File: "a_filename", Could not find the file." >> OUTFILE;
			}
		}
	}
}
