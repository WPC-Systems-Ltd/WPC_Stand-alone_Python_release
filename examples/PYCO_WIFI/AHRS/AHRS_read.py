'''
AHRS - AHRS_read.py.

This example demonstrates the process of obtaining AHRS three axis estimation data.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
sampling_period = 0.005

## Set general setting
pywpc.AHRS_setSamplingPeriod(sampling_period)

## AHRS start
pywpc.AHRS_start()

## Get AHRS three axis estimation
print(pywpc.AHRS_getOrient())