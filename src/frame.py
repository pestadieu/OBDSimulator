#!/usr/bin/python3

class frame(object):
	
	# CAN frame packing/unpacking (see `struct can_frame` in <linux/can.h>)
	can_frame_fmt = "=IB3x8s"
	
	# OBD query/response packing/unpacking (see  `https://en.wikipedia.org/wiki/CAN_bus#Data_frame`)
	obd_frame_fmt = ""

	outbound_can_id = 0x7E8
	
	def __init__(self):
		pass
	
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
