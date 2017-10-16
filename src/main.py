#!/usr/bin/python3

import socket
import struct
import sys

sys.path.append("./obd_pid")

from server import *

s = CANServer()
s.listen("vcan0")

