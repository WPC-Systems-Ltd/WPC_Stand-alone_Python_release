'''
System - get_system_info.py.

This example demonstrates how to get system information.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Get driver verion
version = pywpc.Sys_getDriverVersion()
print(version)

## Get driver name
name = pywpc.Sys_getDriverName()
print(name)

## Get serial number
serial_num = pywpc.Sys_getSerialNumber()
print(serial_num)