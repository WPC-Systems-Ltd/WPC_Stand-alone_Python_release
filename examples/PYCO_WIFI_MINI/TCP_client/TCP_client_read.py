'''
TCP_client - TCP_client_read.py.

This example demonstrates how to read data from server

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Paremeters setting
host_ip = "192.168.5.108"   ## The server's hostname or IP address
port = 3333                 ## The port used by the server
read_bytes = 5

## First you should open tcp server

## Open TCP client
pywpc.TCPClient_open(host_ip, port)

## Read bytes from server
data_read = pywpc.TCPClient_read(read_bytes)
print(data_read)

## Close TCP client
pywpc.TCPClient_close()
