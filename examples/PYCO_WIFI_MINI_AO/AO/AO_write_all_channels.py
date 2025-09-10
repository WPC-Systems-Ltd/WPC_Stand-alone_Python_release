'''
AO - AO_write_all_channels.py.

This example demonstrates the process of writing AO signal.
It outlines the procedure for writing digital signals simultaneously to the AO pins.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Write AO data simultaneously
voltage_list = [-10, -7.5, -5, -2.5, 3.5, 5.5, 7.5, 10]
status = pywpc.AO_writeAllChannels(voltage_list)
print("AO_writeAllChannels status: ", status)