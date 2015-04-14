#!/usr/bin/python

"""
Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn."

[1,2,3,Linked,5,In,7,Linked,9,10,11,LinkedIn]
"""


a = []
for i in range(1,101):
    if (i%4) ==0 and (i%6)==0: # swap conditions wiht 9 and 13
       a.append("LinkedIn")
    elif (i%6) ==0:
        a.append("In")
    elif (i%4)==0: # this line
        a.append("Linked")
    else:
       a.append(i)
print a

