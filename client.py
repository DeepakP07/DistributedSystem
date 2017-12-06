# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:12:41 2017

@author: deepa
"""

import sys
import socket
import struct
import random

class Client():

	#List of valid commands
	commands = ["READ FILE", "WRITE FILE", "PWDIR", "CHDIR", "LS", "QUIT"]

	def __init__(self, port):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.5)
		# Convert an IP address from 32-bit packed binary format to string format and Generate a random color hex
		self.ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))     
		self.port = port
		s.connect(("0.0.0.0", self.port))

		valid = False

		while 1:

			while not valid:
				self.message = raw_input(">: ")
				if any(x in self.message for x in self.commands):
					valid = True
				else:
					print ("Invalid Command\n")
			s.sendall(self.message)
			if self.message == "QUIT":
				sys.exit()
			try:
				recv_data = s.recv(4096)
				print (recv_data + '\n')
				valid = False;
			except socket.timeout:
				print ("Something went wrong\n")
