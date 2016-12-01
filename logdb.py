#!/usr/bin/env  python
import os
import time
import re
import pymysql

def conn_db(ip,date,method,request,status,bodyBytesSent,refer,userAgent):
	cmd="insert into test_log(ip,date,method,request,status,bodyBytesSent,refer,userAgent) values('%s','%s','%s','%s','%s','%s','%s','%s')" %(ip,date,method,request,status,bodyBytesSent,refer,userAgent)
	conn = pymysql.connect(host='xxx.xxx.xxx.xxx', port=3306, user='xxxx', passwd='xxxx',db='xxxx')
	cur = conn.cursor()
	cur.execute(cmd) 
	conn.commit()
	conn.close()

def parsetime(date, month, year, log_time):
    time_str = '%s%s%s %s' %(year, month, date, log_time)  
    return time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(time_str, '%Y%b%d %H:%M:%S'))


def follow(thefile):
	thefile.seek(0,2)
	while True:
		line=thefile.readline()
		if not line:
			time.sleep(2)
			continue
		yield line

ip = r"?P<ip>[\d.]*"
date = r"?P<date>\d+"
month = r"?P<month>\w+"
year = r"?P<year>\d+"
log_time = r"?P<time>\S+"
method = r"?P<method>\S+"
request = r"?P<request>\S+"
status = r"?P<status>\d+"
bodyBytesSent = r"?P<bodyBytesSent>\d+"
refer = r"""?P<refer>
         [^\"]*
         """
userAgent=r"""?P<userAgent>
            .*
           """
p = re.compile(r"(%s)\ -\ -\ \[(%s)/(%s)/(%s)\:(%s)\ [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)\ \"(%s)\"\ \"(%s).*?\"" %( ip, date, month, year, log_time, method, request, status, bodyBytesSent, refer, userAgent ), re.VERBOSE)

f=open(r'D:\nginx-1.8.1\logs\001.cn.access.log','r')
loglines = follow(f)
for line in loglines:
	m = p.search(line)
	if m:
		#print(m.group(1),m.group(2),m.group(3),m.group(4),m.group(5),m.group(6),m.group(7),m.group(8),m.group(9),m.group(10),m.group(11))
		x = parsetime(m.group(2), m.group(3), m.group(4), m.group(5))
		conn_db(m.group(1),x,m.group(6),m.group(7),m.group(8),m.group(9),m.group(10),m.group(11))
