#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import socket
import struct
import sys

from obd_simulator_data import *

def build_can_frame(can_id, data):
	can_dlc = len(data)
	data = data.ljust(8, b'\x00')
	a = struct.pack(can_frame_fmt, can_id, can_dlc, data)
	return a

def recieve_can_frame(socket):
	frame, addr = socket.recvfrom(16)
	can_id, can_dlc, data = struct.unpack(can_frame_fmt, frame)
	return data[3:can_dlc]
	
def send_recv_obd_frame(obd_pid):
	s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
	s.bind((network_interface,))
	try:
		if(obd_pid == 0x0A):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x0a'))
		elif(obd_pid == 0x0D):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x0d'))
		elif(obd_pid == 0x67):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x67'))
		elif(obd_pid == 0x0C):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x0c'))
	except socket.error:
		print('Error sending CAN frame')
	data = recieve_can_frame(s)
	return data

if( __name__ == "__main__" ):

	speed = send_recv_obd_frame(vehicle_speed_pid)	
	print("Car Speed (0x0D): " + str(int.from_bytes(speed, byteorder='big')) +" km/h")
	
	pressure = send_recv_obd_frame(fuel_pressure_pid)
	print("Fuel pressure (0x0A): " + str(3*int.from_bytes(pressure, byteorder='big')) +" kPa")

	rpm = send_recv_obd_frame(engine_rpm_pid)
	print("Engine RPM (0x0C): " + str(int.from_bytes(rpm, byteorder='big')) +" rpm")
	
	temp = send_recv_obd_frame(engine_coolant_temperature_pid)
	print("Engine Coolant Temperature (0x67): " + str(int.from_bytes(temp, byteorder='big')) +" °C")

