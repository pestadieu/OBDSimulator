#!/usr/bin/python3

from obd_pid import *

class EngineRPM(OBDPID):
	self.mode = 1
	self.pid = 0x0C
	
	def __init__():
		pass
	
	def getOBDData(self):
		return 0x0004
