#!/usr/bin/python3

import socket
import sys

from debug import *
from can_frame_outbound import *
from can_frame_inbound import *

class can_server(object):
	
	def listen(self, interface):
		s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
		s.bind((interface,))
		while True:
			print("Server is listening on " + interface)
			can_frame, addr = s.recvfrom(16)
			print_frame("Inbound CAN frame: ", can_frame)
			can_frame_in = can_frame_inbound(can_frame)
			can_frame_out = can_frame_in.get_response()
			
			print_frame("Outbound CAN frame: ", can_frame_out.getFrame())
			s.send(can_frame_out.getFrame())
