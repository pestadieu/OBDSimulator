#!/usr/bin/python3

from obd_pid import *

class vehicle_speed(obd_pid):
	mode = 1
	pid = 0x0D
	
	def __init__(self):
		self.pid = vehicle_speed.pid
		self.mode = vehicle_speed.mode
		pass
	
	def get_pid(self):
		return self.pid
	
	def get_obd_data(self):
		return 0x45
	
