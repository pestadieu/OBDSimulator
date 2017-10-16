#!/usr/bin/python3

from obd_pid import *

class vehicle_speed(OBDPID):
	self.mode = 1
	self.pid = 0x0D
	
	def __init__():
		pass
	
	def getOBDData(self):
		return 0x45
	
	
