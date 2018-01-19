#!/usr/bin/python3

# ~ import logging

from can_server import *

if __name__ == '__main__':
	s = can_server()
	s.listen("vcan0")


