
'''
System - Set_Wifi_info.py.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Set IP
pywpc.Sys_setWifiSSID("your_SSID_name")
pywpc.Sys_setWifiPassword("your_password")

## Reboot PYCO
pywpc.Sys_reboot()

