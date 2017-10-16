#!/usr/bin/python3

import struct

from frame import *

class CANFrameOutbound(Frame):
	
	#TODO Gestion des flags
	def __init__(self, can_id, obd_mode, obd_pid, obd_data):
		super().__init__()
		
		self.odb_len = len(odb_data)
		self.obd_frame_fmt = "=" + obd_len + "s"
		self.odb_mode = odb_mode
		self.odb_pid = odb_pid
		self.odb_data = odb_data
		self.can_data = struct.pack(self.obd_frame_fmt, odb_len, odb_pid, odb_data)
		
		self.can_id = outbound_can_id
		self.can_dlc = len(can_data)
		self.can_data = data.ljust(8, b'\x00')
		self.can_frame = struct.pack(self.can_frame_fmt, can_id, can_dlc, can_data)
	

