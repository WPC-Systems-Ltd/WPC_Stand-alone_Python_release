'''
TCP_client - TCP_client_writeU8List.py.

This example demonstrates how to write u8 list to server

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Paremeters setting
host_ip = "192.168.5.108"   ## The server's hostname or IP address
port = 3333                 ## The port used by the server

## First you should open tcp server

## Open TCP client
pywpc.TCPClient_open(host_ip, port)

## Write U8 list to server
pywpc.TCPClient_writeU8List([0x00, 0x01, 0x02, 0x03])

## Close TCP client
pywpc.TCPClient_close()
