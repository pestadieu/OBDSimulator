#!/usr/bin/python3

from debug import *

Lmode = []
Lpid = []
Lvalue = []

#### Vehicle Speed ####
# Mode: 1
Lmode += [0x01]
# PID: 0x0D
Lpid += [0x0D]
# Value
Lvalue += [45] 
# ~ Lvalue = [15] 

##### Engine RPM ####
# Mode: 1
Lmode += [0x01]
# PID: 0x0C
Lpid += [0x0C]
# Value: (256*byte1+byte2)/4 = 193
Lvalue += [193]

##### Fuel Pressure ####
# Mode: 1
Lmode += [0x01]
# PID: 0x0A
Lpid += [0x0A]
# Value: 3*byte = 75
Lvalue += [75]

#### Engine Coolant Temperature ####
# Mode: 1
Lmode += [0x01]
# PID: 0x05
Lpid += [0x05]
# Value: byte-40 = 25
Lvalue += [25]

def set_value(mode, pid, value):
	for k in range(0, len(Lmode)):
		if((mode == Lmode[k]) and (pid == Lpid[k])):
			Lvalue[k] = value
			return;

	print("PID " + str(hex(pid)) + " on mode " + str(hex(mode)) + " isn't supported")
	return(-1)

def get_response(mode, pid):
	for k in range(0, len(Lmode)):
		if((mode == Lmode[k]) and (pid == Lpid[k])):
			if (pid == 0x0d):
				print(Lvalue[k])
			return(Lvalue[k])
	print("PID " + str(hex(pid)) + " on mode " + str(hex(mode)) + " isn't supported")
	return(-1)
