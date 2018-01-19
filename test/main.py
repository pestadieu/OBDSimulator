#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import socket
import struct
import sys

can_frame_fmt = "=IB3x8s"
can_frame_size = 8
can_broadcast_addr = 0x7DF

network_interface = "vcan0"

fuel_pressure_pid = 0x0A
engine_coolant_temperature_pid = 0x05
vehicle_speed_pid = 0x0D
engine_rpm_pid = 0x0C

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
		elif(obd_pid == 0x05):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x05'))
		elif(obd_pid == 0x0C):
			s.send(build_can_frame(can_broadcast_addr, b'\x02\x01\x0c'))
		else:
			print("Unknown pid")
	except socket.error:
		print('Error sending CAN frame')
	data = recieve_can_frame(s)
	return data

def retreive_speed():
	print("retrieve speed")
	speed = send_recv_obd_frame(0x0D)
	speed = str(hex(int.from_bytes(speed, byteorder='big')))
	return(speed[::2])

def retreive_rpm():
	print("retrieve rpm")
	rpm = send_recv_obd_frame(0x0C)
	rpm = str(256 * hex(int.from_bytes(rpm[0], 'big')) + hex(int.from_bytes(rpm[1], 'big'))/4)
	return(rpm[::2])

def retreive_engine_temp():
	print("retrieve engine temp")
	engine_coolant_temp = send_recv_obd_frame(0x05)
	engine_coolant_temp = rpm = str(hex(int.from_bytes(rpm, 'big')) - 0x40)
	return(engine_coolant_temp[::2])

def retreive_fuel_pressure():
	print("retrieve fuel pressure")
	fuel_pressure = send_recv_obd_frame(0x0A)
	fuel_pressure = str(3*hex(int.from_bytes(fuel_pressure, byteorder='big')))
	return(fuel_pressure[::2])
	
if( __name__ == "__main__" ):

	print("Car Speed (0x0D): " + retreive_speed() +" km/h")
	
	print("Fuel pressure (0x0A): " + retreive_fuel_pressure() +" kPa")

	print("Engine RPM (0x0C): " + retreive_rpm() +" rpm")
	
	print("Engine Coolant Temperature (0x05): " + retreive_engine_temp() +" °C")

