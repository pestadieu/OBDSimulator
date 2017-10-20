#!/usr/bin/python3

import struct

from frame import *
from debug import *

class can_frame_outbound(frame):
	
	#TODO Gestion des flags
	def __init__(self, can_id, obd_mode, obd_pid, obd_data):
		self.obd_len = len(obd_data) + 2
		self.obd_mode = obd_mode
		self.obd_pid = obd_pid
		self.obd_data = obd_data.ljust(5, b'\x00')
		frame.obd_frame_fmt = "=bbb5b"
		self.can_data = struct.pack(frame.obd_frame_fmt, self.obd_len, self.obd_mode,  self.obd_pid, self.obd_data[0], self.obd_data[1], self.obd_data[2], self.obd_data[3], self.obd_data[4])
		print_frame("OBD response: ", self.can_data)
		
		can_dlc = self.obd_len + 1
		self.can_frame = struct.pack(frame.can_frame_fmt, can_id, can_dlc, self.can_data)
	

