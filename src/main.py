#!/usr/bin/python3

#import socket
#import struct
#import sys

#sys.path.append("./obd_pid")

#from obd_pid import *
from can_server import *

s = can_server()
s.listen("vcan0")

