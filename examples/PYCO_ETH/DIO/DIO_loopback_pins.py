'''
DIO - DIO_loopback_pins.py.

This example shows how to use DIO loopback with pins.
It involves using DO pins to send signals and DI pins to receive signals on a single device, commonly known as "loopback".
It performs the operation of writing to a DO pin and reading from a DI pin.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
DO_pins = [0, 1, 2, 3]
DI_pins = [4, 5, 6, 7]
pin_state = [1, 1, 0, 0]

## Write pins to high or low
status = pywpc.DO_writePins(DO_pins, pin_state)
print("DO_writePins status: ", status)

## Read DI pins state
status = pywpc.DI_readPins(DI_pins)
print("DI_readPins status: ", status)
