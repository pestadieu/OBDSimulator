#!/usr/bin/python3

import struct

from frame import *
from obd_pid import *

class CANFrameInbound(Frame):
	
	def __init__(self, can_frame):
		super().__init__()
		# Dissect the frame
		self.can_frame = can_frame
		self.can_id, self.can_dlc, self.can_data = struct.unpack(self.can_frame_fmt, can_frame)
		self.obd_len, self.obd_mode, self.obd_pid, self.obd_data = struct.unpack(self.obd_frame_fmt, self.can_data)
		
	def getResponse(self):
		res = OBDPID(self.obd_mode, self.obd_pid)
		f_out = CANFrameOutbound(self.outbound_can_id, self.obd_mode, res.getOutboundOBDPid(), res.getOBDData())
		return f_out.getFrame()
