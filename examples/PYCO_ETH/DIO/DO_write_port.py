'''
DIO - DO_write_pins.py.

This example shows how to write high or low signal to DO port.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
pin_state = [1, 0, 1, 0, 1, 0, 1]

## Write port to high or low
status = pywpc.DO_writePort(pin_state)
print("DO_writePort status: ", status)
