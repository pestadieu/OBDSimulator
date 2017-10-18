#!/usr/bin/python3

class obd_pid(object):
	def __init__(self):
		pass
	
	def get_outbound_pid(self):
		return hex(self.pid + 0x40)
	
	def get_pid(self):
		return self.pid
	
	def get_obd_data(self):
		pass
	
	def get_data_length(self):
		return len(self.get_data())
