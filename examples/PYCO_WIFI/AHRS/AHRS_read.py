'''
AHRS - AHRS_read.py.

This example demonstrates the process of obtaining AHRS three axis estimation data.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
theo_grav = 9.81
dt = 0.005
offset_z = 0.005

## Set general setting
pywpc.AHRS_setGeneral(theo_grav, dt, offset_z)

## AHRS start
pywpc.AHRS_start()

## Get AHRS three axis estimation
print(pywpc.AHRS_getOrient())