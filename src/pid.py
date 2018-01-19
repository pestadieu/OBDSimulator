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
Lvalue += [b'\x45'] 
# ~ Lvalue = [b'\x15'] 

##### Engine RPM ####
# Mode: 1
Lmode += [0x01]
# PID: 0x0C
Lpid += [0x0C]
# Value: (256*byte1+byte2)/4 = 193
Lvalue += [b'\x03\x04']

##### Fuel Pressure ####
# Mode: 1
Lmode += [0x01]
# PID: 0x0A
Lpid += [0x0A]
# Value: 3*byte = 75
Lvalue += [b'\x25']

#### Engine Coolant Temperature ####
# Mode: 1
Lmode += [0x01]
# PID: 0x05
Lpid += [0x05]
# Value: byte-40 = 25
Lvalue += [b'\x65']

# ~ Lmode = [vs_mode, er_mode, fp_mode, ect_mode]
# ~ Lpid = [vs_pid, er_pid, fp_pid, ect_pid]
# ~ Lvalue = [vs_value, er_value, fp_value, ect_value]

def get_response(mode, pid):
	for k in range(0, len(Lmode)):
		if((mode == Lmode[k]) and (pid == Lpid[k])):
			return(Lvalue[k])
	print("PID " + str(hex(pid)) + " on mode " + str(hex(mode)) + " isn't supported")
	return(-1)
