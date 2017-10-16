#!/usr/bin/python3

import sys

DEBUG = 1

def printd(*objects, sep=' ', end='\n', file=sys.stdout):
	if(DEBUG):
		print(*objects, sep=' ', end='\n', file=sys.stdout)
		
def print_frame(msg, frame):
	ch = "0000  "
	count = 0
	if(DEBUG):
		for k in range(0, len(frame)):
			ch += format(frame[k], '02x')
			if(count == 15):
				ch += "\n00" + (k//16) + "0  "
				count = 0
			elif(count == 7):
				ch += " "
			count ++
			ch += " "
		print(msg)
		print(ch)
