#!/usr/bin/awk -f 
BEGIN{
    
}

{
	
	gsub(/\"/, "", $5)
	gsub(/\"/, "", $6)
	parse1 = $5"&"$6
	parse_query(parse1,result);
	vid = result["vid"];
	guid = result["guid"];
	print vid " " guid;
}

END{
    
}

function parse_query(str,array) {
    delete array;
    split(str,arr,"&");
    for(i=1;i<=length(arr);i++) {
        split(arr[i],tmp,"=");
        if(length(tmp) > 2){
	        tmp_offset = index(arr[i],"=");
	        array[tmp[1]] = substr(arr[i],tmp_offset,length(arr[i]) - length(tmp[1]));
        }else if(length(tmp) == 2){
		array[tmp[1]] = tmp[2];
        }else{
		#array[tmp[1]] = tmp[2];
	}
    }
}
