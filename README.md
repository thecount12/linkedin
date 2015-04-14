# LinkedIn Collabedit Test
=======
<b>First Problem</b>

Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn."


see firstprob.py for complete solution

When I started working on this probject I worked on "Linked" and "In" before 
undertaking "LinkedIn". So while I had 99% of this completed. I had operations
for 4 and 6 together out of order for the final "LinkedIn" print statement. I 
received credit on this before proceeding to the next problem. 

<b>Second Problem</b>

I decided to paste in part of this problem for your review. secondprob.py has 
completed solution 

	---------- begin sample log extract ----------
	Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
	Jan 20 03:25:09 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate
	Jan 20 03:26:21 fakehost anacron[28969]: Job 'cron.daily' terminated
	Jan 20 03:26:22 fakehost anacron[28969]: Normal exit (1 job run)
	Jan 20 03:30:01 fakehost CROND[31462]: (root) CMD (/usr/lib64/sa/sa1 1 1)
	Jan 20 03:30:01 fakehost CROND[31461]: (root) CMD (/var/system/bin/sys-cmd -F > /dev/null 2>&1)

Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages

	---------- begin sample output ----------
	minute, number_of_messages
	Jan 20 03:25,2
	Jan 20 03:26,2
	Jan 20 03:30,2
	Jan 20 05:03,1
	Jan 20 05:20,1
	Jan 20 05:22,6
	---------- end sample output ----------

The result of my code was incomplete. I had a suggestion of building a token to 
keep track of the log hours which might have proved more difficult later on. 
He suggested "counter_dict=collections.defaultdict(int)". Once he suggested using
a dictionary to keep track of the log files hour. I defined bdict={}
and suggested applying the string to the dictionary if it didn't exist and incrementing
it if it already did. But it was not able to complete it in time.

	num=0
	counter_dict = collections.defaultdict(int)
	bdict={}
	f=open("log.txt")
	
	for i in f.readlines():
    		num+=1
    		if 'fakehost' in i:
        		dat=i.split("fakehost")
        		time=dat[0].split(":")
        		counter_dict[time[0]+':'time[1]] += 1
        		if time[1] not in dict.keys(bdit):
            			bdict[i]=1
        		#print dat[0],",",num

Obviously the code above was incomplete I valued the suggestion of a dictionary 
but didn't like the direction he was heading. My final solutions proves better.  

<b>Notes</b>

The problem with these types of tests while they might seem trivial after the fact it
does not prove your ability as a software developer to code, see the big picture, work
in triage, lead or work in a team envrionment.  

I look forward to your responses

Regards, 
William Gunnells
gunnells@gmail.com


 
