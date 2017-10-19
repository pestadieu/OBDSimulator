#!/usr/bin/python3

from obd_pid.vehicle_speed import *
from obd_pid.engine_rpm import *
from debug import *

class obd_pid(object):
	def __init__(self):
		self.L = []
		self.L += [vehicle_speed()]
		self.L += [engine_rpm()]
	
	def get(self, mode, pid):
		if(mode == 1):
			for c in self.L:
				if(pid == c.get_pid()):
					printd("PID " + str(c.get_pid()) + " is " + c.__str__())
					return c
			printd("PID " + str(hex(pid)) + " isn't supported")
		else:
			printd("Mode " + str(hex(mode)) + " isn't supported")
	
	
	
