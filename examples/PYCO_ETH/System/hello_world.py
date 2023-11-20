'''
System - hello world.py.

This example code is in the public domain from PYCO_WIFI.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Python
import time
import machine

for i in range(10, 0, -1):
    print(f"Restarting in {i} seconds...")
    time.sleep(1) ## delay [s]
print(f"Restarting now")

## Reboot device
machine.reset()
