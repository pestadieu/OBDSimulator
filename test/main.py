#!/usr/bin/python3

import socket
import struct
import sys

can_frame_fmt = "=IB3x8s"

def build_can_frame(can_id, data):
	can_dlc = len(data)
	data = data.ljust(8, b'\x00')
	a = struct.pack(can_frame_fmt, can_id, can_dlc, data)
	#print(a)
	return a
	
def test_vehicle_speed():
	s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
	s.bind(("vcan0",))
	try:
		s.send(build_can_frame(0x7DF, b'\x02\x01\x0d'))
		#s.send(b'\x07\xdf\x00\x00\x03\x00\x00\x00\x02\x01\x0C\x00\x00\x00\x00\x00')
	except socket.error:
		print('Error sending CAN frame')
	frame, addr = s.recvfrom(16)
	can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
	return data[3:can_dlc]

def test_engine_rpm():
	s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
	s.bind(("vcan0",))
	try:
		s.send(build_can_frame(0x7DF, b'\x02\x01\x0c'))
		#s.send(b'\x07\xdf\x00\x00\x03\x00\x00\x00\x02\x01\x0C\x00\x00\x00\x00\x00')
	except socket.error:
		print('Error sending CAN frame')
	frame, addr = s.recvfrom(16)
	can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
	return data[3:can_dlc]

speed = test_vehicle_speed()
print("Your car is going at " + str(int.from_bytes(speed, byteorder='big')) +" km/h")

rpm = test_engine_rpm()
a, b = struct.unpack("=bb", rpm)
#print(str(a) + " " + str(b))
print("Your engine is at " + str((256*a+b)/4) +" rpm")


