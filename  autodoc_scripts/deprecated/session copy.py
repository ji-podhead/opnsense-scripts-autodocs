#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import socket
#sys.path.insert(0, '/usr/local/opnsense/service')
#print(sys.path)
#print(os.path.abspath(__file__))
#from configd import get_config
configd_socket_name = '/var/run/configd.socket'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect(configd_socket_name)
sock.send(("get_config").encode())
#config=get_config()

#print(config)