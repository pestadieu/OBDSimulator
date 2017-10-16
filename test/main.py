#!/usr/bin/python3

import socket
import struct
import threading
import sys

sys.path.append("../src/server.py")

from server.py import *

"""class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		s = CANServer()
		s.listen("vcan0")"""
      
can_frame_fmt = "=IB3x8s"

def build_can_frame(can_id, data):
	can_dlc = len(data)
	data = data.ljust(8, b'\x00')
	a = struct.pack(can_frame_fmt, can_id, can_dlc, data)
	print(a)
	return a
	
def test():
	s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
	s.bind(("vcan0",))
	try:
		#s.send(build_can_frame(0x01, b'\x01\x02\x03'))
		#s.send(b'\x01\x00\x00\x00\x03\x00\x00\x00\x01\x01\x03\x00\x00\x00\x00\x00')
		s.send(b'\x07\xdf\x00\x00\x03\x00\x00\x00\x02\x01\x0C\x00\x00\x00\x00\x00')
	except socket.error:
		print('Error sending CAN frame')

test()
