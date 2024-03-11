'''
AHRS - AHRS_read.py.

This example demonstrates the process of obtaining AHRS three axis estimation data.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## AHRS start
pywpc.AHRS_start()

##  Get AHRS's 3 axis orientation.
print(pywpc.AHRS_getOrientation())

##  Get AHRS's 3 axis angular velocity.
print(pywpc.AHRS_getAngularVelocity())

##  Get AHRS's 3 axis acceleration.
print(pywpc.AHRS_getAcceleration())