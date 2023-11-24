'''
DIO - DO_write_pins.py.

This example shows how to write high or low signal to DO port.
There are 6 pins for DO

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
pin_state = [1, 0, 1, 0, 1, 0]

## Write port to high or low
status = pywpc.DO_writePort(pin_state)
print("DO_writePort status: ", status)
