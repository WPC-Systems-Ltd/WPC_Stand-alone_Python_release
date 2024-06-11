'''
AHRS - AHRS_read.py.

This example demonstrates the process of obtaining AHRS three axis estimation data.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Python
import time

## AHRS start
pywpc.AHRS_start()

time.sleep(1)

## Get AHRS's 3 axis orientation.
print(pywpc.AHRS_getOrientation())

## Get AHRS's 3 axis angular velocity.
print(pywpc.AHRS_getAngularVelocity())

## Get AHRS's 3 axis acceleration.
print(pywpc.AHRS_getAcceleration())

## AHRS stop
pywpc.AHRS_stop()