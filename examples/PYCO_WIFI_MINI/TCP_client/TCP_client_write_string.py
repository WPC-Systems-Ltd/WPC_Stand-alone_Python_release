'''
TCP_client - TCP_client_write_string.py.

This example demonstrates how to write string to server

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

## Write string to server
pywpc.TCPClient_writeString("Hello world")
pywpc.TCPClient_writeString("WPC Systems Ltd.")
pywpc.TCPClient_writeString("Good day")

## Close TCP client
pywpc.TCPClient_close()

