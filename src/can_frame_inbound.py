#!/usr/bin/python3

import struct

from frame import *
from can_frame_outbound import *
from obd_pid.obd_pid import *
from debug import *

class can_frame_inbound(frame):
	
	def __init__(self, can_frame):
		self.can_frame = can_frame
		self.can_id, self.can_dlc, self.can_data = struct.unpack(self.can_frame_fmt, can_frame)
		print_frame("OBD query: ", self.can_data)
		#frame.obd_frame_fmt = "="+"b"*3 + "5b"
		frame.obd_frame_fmt = "=bbb5b"
		a = struct.unpack(self.obd_frame_fmt, self.can_data)
		self.obd_len = a[0]
		self.obd_mode = a[1]
		self.obd_pid = a[2]
		printd("OBD pid = " + str(self.obd_pid))
		
	def get_response(self, obd_pid):
		res = obd_pid.get(self.obd_mode, self.obd_pid)
		f_out = can_frame_outbound(frame.outbound_can_id, self.obd_mode, res.get_outbound_pid(), res.get_obd_data())
		return f_out
