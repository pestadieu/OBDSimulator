#!/usr/bin/python3

class engine_rpm(object):
	mode = 1
	pid = 0x0c
	
	def __init__(self):
		self.pid = engine_rpm.pid
		self.mode = engine_rpm.mode
	
	def __str__(self):
		return "engine rpm"
	
	def get_obd_data(self):
		return b'\x03\x04'

	def get_pid(self):
		return self.pid
	
	def get_outbound_pid(self):
		#return hex(self.pid + 0x40)
		return 0x4c
	
	def get_data_length(self):
		return len(self.get_obd_data())
