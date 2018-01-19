#!/usr/bin/python3

from pid.pid_data import *
from debug import *

# ~ class pid(object):
	
	# ~ Lmode = [vs_mode, er_mode, fp_mode, ect_mode]
	# ~ Lpid = [vs_pid, vs_pid, fp_pid, ect_pid]
	# ~ Lvalue = [vs_value, er_value, fp_value, ect_value]
	
	# ~ def __init__(self):
		# ~ config = ConfigParser()
		# ~ config.read('obd_pid.ini')
		# ~ self.obd_str = config.sections()
		# ~ print(self.obd_str)
		# ~ self.obd_mode = [vs_mode, er_mode, fp_mode, ect_mode]
		# ~ self.obd_pid = [vs_pid, vs_pid, fp_pid, ect_pid]
		# ~ self.obd_value = [vs_value, er_value, fp_value, ect_value]
		
		# ~ for k in config.sections():
			# ~ self.obd_mode += [config.get(k, 'mode')]
		# ~ print(self.obd_mode)
		# ~ for k in config.sections():
			# ~ self.obd_pid += [config.get(k, 'pid')]
		# ~ for k in config.sections():
			# ~ self.obd_value += [config.get(k, 'value')]
		# ~ print("pid initialized")
	
	# ~ def get_response(self, mode, pid):
		# ~ for k in range(0, len(Lmode)):
			# ~ if((mode == self.Lmode[k]) and (pid == self.Lpid[k])):
				# ~ return(self.Lvalue[k])
				
		# ~ printd("PID " + str(hex(pid)) + " on mode " + str(hex(mode)) + " isn't supported")
		# ~ return(-1)
	
Lmode = [vs_mode, er_mode, fp_mode, ect_mode]
Lpid = [vs_pid, er_pid, fp_pid, ect_pid]
Lvalue = [vs_value, er_value, fp_value, ect_value]

def get_response(mode, pid):
	for k in range(0, len(Lmode)):
		if((mode == Lmode[k]) and (pid == Lpid[k])):
			return(Lvalue[k])
			
	print("PID " + str(hex(pid)) + " on mode " + str(hex(mode)) + " isn't supported")
	return(-1)
