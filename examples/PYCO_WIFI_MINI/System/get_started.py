'''
System - get_started.py.

This example demonstrates how to reboot the device

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Python
import time

print(f"Hello world!")

for i in range(10, 0, -1):
    print(f"Restarting in {i} seconds...")
    time.sleep(1) ## delay [s]

print(f"Restarting now")
pywpc.Sys_reboot()