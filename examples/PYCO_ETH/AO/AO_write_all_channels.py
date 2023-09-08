'''
AO - AO_write_all_channels.py.

This example demonstrates the process of writing AO signal.
It outlines the procedure for writing digital signals simultaneously to the AO pins.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Write AO data simultaneously
voltage_list = [-10, -7.5, -5, -2.5, 3.5, 5.5, 7.5, 10]
status = pywpc.AO_writeAllChannels(voltage_list)
print("AO_writeAllChannels status: ", status)
