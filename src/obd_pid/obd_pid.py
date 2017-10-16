#!/usr/bin/python3

class OBDPID(object):
	
	def __init__(self, obd_mode, obd_pid):
		
		if(obd_mode == 1):
			switch(obd_pid):
				case 0x0D:
					return VehiculeSpeed(obd_mode, obd_pid)
					break
				case 0x0C:
					return EngineRPM(obd_mode, obd_pid)
					break
				default:
					printd("PID" + obd_pid + "isn't registered")
	
	def getOutboundODBPid(self):
		return hex(self.pid + 0x40)
	
	def getODBPid(self):
		return self.pid
	
	def getOBDData(self):
		pass
	
	def getOBDDataLength(self):
		return len(self.getOBDData())
