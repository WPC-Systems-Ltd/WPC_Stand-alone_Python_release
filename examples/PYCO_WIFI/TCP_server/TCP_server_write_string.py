'''
TCP_server - TCP_server_write.py.

This example demonstrates how to write string via tcp server
It should connect wifi before tcp connection

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Paremeters setting
port = 5566
write_data = "Hello_world"

## Open TCP with port
pywpc.TCPServer_open(port)

## Write string
pywpc.TCPServer_writeString(write_data, len(write_data))

## Close TCP
pywpc.TCPServer_close()
