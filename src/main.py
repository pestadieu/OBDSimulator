#!/usr/bin/python3

from can_server import *

s = can_server()
s.listen("vcan0")

