#!/usr/bin/python3

# ~ import logging

from can_server import *

if __name__ == '__main__':
	# ~ logging.basicConfig(filename='OBDSimulator.log', level=logging.DEBUG)
	s = can_server()
	s.listen("vcan0")


