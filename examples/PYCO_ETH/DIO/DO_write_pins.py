'''
DIO - DO_write_pins.py.

This example shows how to write high or low signal to DO pin.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
pin_index  = [4, 5, 6]
pin_state  = [1, 1, 1]

## Write pins to high or low
status = pywpc.DO_writePins(pin_index, pin_state)
print("DO_writePins status: ", status)
