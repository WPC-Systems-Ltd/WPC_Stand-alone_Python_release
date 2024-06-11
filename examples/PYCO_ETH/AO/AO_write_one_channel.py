'''
AO - AO_write_one_channel.py with.

This example demonstrates the process of writing AO signal.
It outlines the procedure for writing digital signals with channel to the AO pins.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Write AO 1.5(V) in channel 0
ch0 = 0
voltage0 = 1.5
status = pywpc.AO_writeOneChannel(ch0, voltage0)
print("AO_writeOneChannel status: ", status)