#!/usr/bin/env python3

# This script simply adds a timestamp to any file to the front of the filename. 
# Works in Linux, may work in Windows & Mac

import os, time, sys
months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
for i in sys.argv[1:]:
	ctime = time.ctime(os.path.getctime(i)).split()
	ifile = i[22:] if sys.argv[1][20:22] == "]_" else i
	os.system(f'mv \"{ifile}\" \"[{ctime[4]}-{months[ctime[1]]}-{ctime[2].zfill(2)}_{ctime[3].replace(":","-")}]_{ifile}\"')
