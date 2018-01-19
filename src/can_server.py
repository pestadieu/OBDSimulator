#!/usr/bin/python3

import socket

from debug import *
from can_frame import *
from pid import *

class can_server(object):
	
	def __init__(self):
		pass
		
	def listen(self, interface):
		s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
		s.bind((interface,))
		while True:
			print("Server is listening on " + interface)
			frame_in, addr = s.recvfrom(16)
			print_frame("Inbound CAN frame: ", frame_in)
			frame_in = can_frame(frame_in)
			can_frame_out = frame_in.build_response()
			
			print_frame("Outbound CAN frame: ", can_frame_out.get_frame())
			s.send(can_frame_out.get_frame())

