'''
TCP_server - TCP_server_read.py.

This example demonstrates how to read data from tcp server
It should connect wifi before tcp connection

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Paremeters setting
port = 5566
read_bytes = 14

## Open TCP with port
pywpc.TCPServer_open(port)

## Read 14 bytes from TCP server
data_read = pywpc.TCPServer_read(read_bytes)
print(data_read)

## Close TCP
pywpc.TCPServer_close()
