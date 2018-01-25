#!/usr/bin/python3

import socket

from debug import *
from can_frame import *
from pid import *
import json
import time

import threading

UPDATE_FREQUENCY = 0.5

class Simulation():
	countUpdateSpeed = 0
	countUpdateRPM = 0
	countUpdateFuelPressure = 0
	countUpdateCoolantTemperature = 0

	speed = [[],[]]
	rpm = [[],[]]
	fuel_pressure = [[],[]]
	coolant_temperature = [[],[]]

	startTime = 0

	def __init__(self, filename):
		with open(filename, 'r') as file:
			data = json.load(file)

		self.speed = data["speed"]
		self.rpm = data["rpm"]
		self.fuel_pressure = data["fuel pressure"]
		self.coolant_temperature = data["coolant temperature"]

		self.countUpdateSpeed = 0
		self.countUpdateRPM = 0
		self.countUpdateFuelPressure = 0
		self.countUpdateCoolantTemperature = 0 

		self.startTime = time.time()

		self.update()

	def setSpeed(self, speed):
		set_value(0x01, 0x0D, bytes([speed]) )

	def setRPM(self, rpm):
		a, b = divmod((rpm*4), 256)
		set_value(0x01, 0x0C, bytes([a, b]))

	def setFuelPressure(self, fuel_pressure):
		
		set_value(0x01, 0x0A, bytes([(int)(fuel_pressure/3)]))

	def setCoolantTemperature(self, coolant_temperature):
		set_value(0x01, 0x05, bytes([coolant_temperature+40]))

	def updateSpeed(self):
		if self.countUpdateSpeed > len(self.speed) - 1: # if bigger than array stop
			return;

		currentTime = time.time()
		if currentTime - self.startTime > self.speed[self.countUpdateSpeed]["time"]:
			print("%.3f : Speed => %i" % (currentTime - self.startTime, self.speed[self.countUpdateSpeed]["value"]) )
			self.setSpeed( self.speed[self.countUpdateSpeed]["value"] )
			self.countUpdateSpeed += 1

	def updateRPM(self):
		if self.countUpdateRPM > len(self.rpm) - 1: # if bigger than array stop
			return;

		currentTime = time.time()
		if currentTime - self.startTime > self.rpm[self.countUpdateRPM]["time"]:
			print("%.3f : RPM => %i" % (currentTime - self.startTime, self.rpm[self.countUpdateRPM]["value"]) )
			self.setRPM( self.rpm[self.countUpdateRPM]["value"])
			self.countUpdateRPM += 1

	def updateFuelPressure(self):
		if self.countUpdateFuelPressure > len(self.fuel_pressure) - 1: # if bigger than array stop
			return;

		currentTime = time.time()
		if currentTime - self.startTime > self.fuel_pressure[self.countUpdateFuelPressure]["time"]:
			print("%.3f : Fuel pressure => %i" % (currentTime - self.startTime, self.fuel_pressure[self.countUpdateFuelPressure]["value"]) )
			self.setFuelPressure( self.fuel_pressure[self.countUpdateFuelPressure]["value"])
			self.countUpdateFuelPressure += 1

	def updateCoolantTemperature(self):
		if self.countUpdateCoolantTemperature > len(self.coolant_temperature) - 1: # if bigger than array stop
			return;

		currentTime = time.time()
		if currentTime - self.startTime > self.coolant_temperature[self.countUpdateCoolantTemperature]["time"]:
			print("%.3f : Coolant temperature => %i" % (currentTime - self.startTime, self.coolant_temperature[self.countUpdateCoolantTemperature]["value"]) )
			self.setCoolantTemperature( self.coolant_temperature[self.countUpdateCoolantTemperature]["value"]) 
			self.countUpdateCoolantTemperature += 1

	def update(self):
		self.updateSpeed()
		self.updateRPM()
		self.updateFuelPressure()
		self.updateCoolantTemperature()



class inputThread (threading.Thread):
	simulation = 0
	def __init__(self):
		self.simulation = Simulation('simulation.json') 
		threading.Thread.__init__(self)

	def run(self):
		while True:
			time.sleep(UPDATE_FREQUENCY)
			self.simulation.update()


class can_server(object):
	def __init__(self):
		pass
		
	def listen(self, interface):
		it = inputThread()
		it.start()

		s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
		s.bind((interface,))
		print("Server is listening on " + interface)
		while True:
			frame_in, addr = s.recvfrom(16)
			# ~ print_frame("Inbound CAN frame: ", frame_in)
			frame_in = can_frame(frame_in)
			can_frame_out = frame_in.build_response()
			
			# ~ print_frame("Outbound CAN frame: ", can_frame_out.get_frame())
			s.send(can_frame_out.get_frame())

