#!/usr/bin/python3

import struct

from pid import *
from debug import *

class can_frame(object):
	
	can_frame_fmt = "=IB3x8s"
	obd_query_fmt = "=bbb5b"
	
	outbound_can_id = 0x7E8
	
	def __init__(self, can_frame):
		self.can_frame = can_frame
		self.can_id, self.can_dlc, self.can_data = struct.unpack(self.can_frame_fmt, can_frame)
		
		# ~ print_frame("OBD query: ", self.can_data)
		obd = struct.unpack(self.obd_query_fmt, self.can_data)
		self.obd_len = obd[0]
		self.obd_mode = obd[1]
		self.obd_pid = obd[2]
		
	def build_response(self):
		# ~ print(self.obd_pid)
		obd_data = get_response(self.obd_mode, self.obd_pid)
		
		# ~ print("OBD data:")
		# ~ print(obd_data[0])
		# ~ print(obd_data[1])
		# ~ print(obd_data[2])
		# ~ print(obd_data[3])
		self.obd_mode += 0x40
		self.obd_len = len(obd_data) + 2
		self.obd_data = obd_data.ljust(5, b'\x00')
		# ~ if (self.obd_pid == 0x0d):
			# ~ print(hex(self.obd_len))
			# ~ print(self.obd_mode)
			# ~ print(hex(self.obd_pid))
			# ~ print("OBD data:")
			# ~ print(self.obd_data[0])
			# ~ print(self.obd_data[1])
			# ~ print(self.obd_data[2])
			# ~ print(self.obd_data[3])
		
		self.can_data = struct.pack(self.obd_query_fmt, self.obd_len, self.obd_mode,  self.obd_pid, self.obd_data[0], self.obd_data[1], self.obd_data[2], self.obd_data[3], self.obd_data[4])
		if (self.obd_pid == 0x0d):
			print_frame("OBD response: ", self.can_data)
		self.can_dlc = self.obd_len + 1
		self.can_frame = struct.pack(self.can_frame_fmt, self.outbound_can_id, self.can_dlc, self.can_data)
		return self
	
	def get_id(self):
		return self.can_id
	
	def get_dlc(self):
		return self.can_dlc
	
	def get_obd_len(self):
		return self.obd_len
	
	def get_obd_mode(self):
		return self.obd_mode
	
	def get_obd_pid(self):
		return self.obd_pid
	
	def get_obd_data(self):
		return self.obd_data
	
	def get_data(self):
		return self.can_data
	
	def get_frame(self):
		return self.can_frame
