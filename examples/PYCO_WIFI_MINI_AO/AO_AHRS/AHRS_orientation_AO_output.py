'''
AO_AHRS - AHRS_orientation_AO_output.py.

This example demonstrates **the real-time mapping and output of AHRS orientation data (Roll, Pitch, Yaw) to the Analog Output (AO) channels.**

The code starts the AHRS system, continuously reads the three orientation angles in radians, and assigns them to specific AO output channels (channels 5, 6, and 7).

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc
import time

## Erase all message on the screen
pywpc.OLED_erase()

## Write in line 1
pywpc.OLED_writeLine("AHRS for AO output", 1)

## Write in line 2
pywpc.OLED_writeLine("CH5:roll(rad)", 2)

## Write in line 3
pywpc.OLED_writeLine("CH6:pitch(rad)", 3)

## Write in line 4
pywpc.OLED_writeLine("CH7:yaw(rad)", 4)

## AHRS start
pywpc.AHRS_start()

## Wait for while
time.sleep(3)

## Create AO default list
old_list = [0, 0, 0, 0, 0, 0, 0, 0]
new_list = [0, 0, 0, 0, 0, 0, 0, 0]

while (1):
    rpy = pywpc.AHRS_getOrientation_rad()
    new_list[5] = rpy[0]  ## pi ~ - pi
    new_list[6] = rpy[1]  ## pi/2 ~ - pi/2
    new_list[7] = rpy[2]  ## pi ~ - pi
    if new_list != old_list:
        old_list = new_list.copy()
        pywpc.AO_writeAllChannels(old_list)