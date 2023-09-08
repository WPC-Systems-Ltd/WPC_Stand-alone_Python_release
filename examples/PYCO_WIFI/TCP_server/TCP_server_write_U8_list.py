'''
TCP_server - TCP_server_write.py.

This example demonstrates how to write u8 list via tcp server
It should connect wifi before tcp connection

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Paremeters setting
port = 5566
new_list = [0x55, 0xAA, 0x55, 0xAA]

## Open TCP with port
pywpc.TCPServer_open(port)

## Write string
pywpc.TCPServer_writeU8List(new_list)

## Close TCP
pywpc.TCPServer_close()
