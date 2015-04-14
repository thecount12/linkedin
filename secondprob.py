#!/usr/bin/python

# load statement below as log.txt
"""
---------- begin sample log extract ----------
Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
Jan 20 03:25:09 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
Jan 20 03:26:22 fakehost anacron[28969]: Normal exit (1 job run)
"""

f=open("log.txt")
ar={} 
for i in f.readlines():
	if 'fakehost' in i: 
		d=i.split("fakehost")
		date=d[0].split(":")
		time=date[0]+":"+date[1] 
		if time not in dict.keys(ar):
			ar[time]=1
		else:
			ar[time]+=1
#print ar
for j in ar:
	print j,",",ar[j]	
