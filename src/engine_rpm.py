#!/usr/bin/python3

from obd_pid import *

class engine_rpm(obd_pid):
	mode = 1
	pid = 0x0c
	
	def __init__(self):
		self.pid = engine_rpm.pid
		self.mode = engine_rpm.mode
		pass
	
	def get_obd_data(self):
		return 0x0004
