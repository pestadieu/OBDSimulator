#!/usr/bin/python3

from engine_rpm import *
from vehicle_speed import *

"""def init_pid():
	L = []
	L += vehicle_speed()
	L += engine_rpm()"""
	
def get(mode, pid):
	
	vs = vehicle_speed()
	er = engine_rpm()
	
	if(mode == 1):
		if(pid == vs.get_pid()):
			return vs
		elif(pid == er.get_pid()):
			return er
		else:
			printd("PID" + pid + "isn't supported")
	else:
		printd("Mode" + mode + "isn't supported")
