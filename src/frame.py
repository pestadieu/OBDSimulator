#!/usr/bin/python3

class Frame(object):
	
	# CAN frame packing/unpacking (see `struct can_frame` in <linux/can.h>)
	can_frame_fmt = "=IB3x8s"
	
	# OBD query/response packing/unpacking (see  `https://en.wikipedia.org/wiki/CAN_bus#Data_frame`)
	obd_frame_fmt = ""
	
	outbount_can_id = 0x7E8
       
	def __init__(self):
		pass
	
	def getId(self):
		return self.can_id
	
	def getDlc(self):
		return self.can_dlc
	
	def getOBDlen(self):
		return self.obd_len
	
	def getOBDMode(self):
		return self.obd_mode
	
	def getOBDPid(self):
		return self.obd_pid
	
	def getOBDData(self):
		return self.obd_data
	
	def getData(self):
		return self.can_data
	
	def getFrame(self):
		return self.can_frame
