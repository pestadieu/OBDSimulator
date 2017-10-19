#!/usr/bin/python3

class vehicle_speed(object):
	mode = 1
	pid = 0x0D
	
	def __init__(self):
		self.pid = vehicle_speed.pid
		self.mode = vehicle_speed.mode

	def __str__(self):
		return "vehicle speed"
	
	def get_pid(self):
		return self.pid
	
	def get_obd_data(self):
		return b'\x45'
	
	def get_outbound_pid(self):
		#return hex(self.pid + 0x40)
		return 0x4D
	
	def get_data_length(self):
		return len(self.get_obd_data())
	
	
		
