#!/usr/bin/python3

import socket
import sys

from debug import *
from frame_outbound import *
from frame_inbound import *

class CANServer(object):
	
	def listen(self, interface):
		s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
		s.bind((interface,))
		while True:
			print("Server is listening")
			can_frame, addr = s.recvfrom(16)
			print_frame("CAN server recieved: ", can_frame)
			can_frame_in = CANFrameInbound(can_frame)
			can_frame_out = can_frame_in.getResponse()
			
			print_frame("CAN server recieved: ", can_frame_out.getFrame())
			s.send(can_frame_out.getFrame())
