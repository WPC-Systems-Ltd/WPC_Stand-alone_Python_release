'''
System - get_network_info.py.

This example demonstrates how to get network information.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Get IP
ip = pywpc.Sys_getIP()
print(ip)

## Get submask
sbk = pywpc.Sys_getSubmask()
print(sbk)

## Get gateway
gateway = pywpc.Sys_getGateway()
print(gateway)

## Get MAC
mac = pywpc.Sys_getMAC()
print(mac)