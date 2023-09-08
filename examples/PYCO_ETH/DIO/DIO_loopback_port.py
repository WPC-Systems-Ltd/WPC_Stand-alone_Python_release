'''
DIO - DIO_loopback_pins.py.

This example shows how to use DIO loopback with port
It involves using DO pins to send signals and DI pins to receive signals on a single device, commonly known as "loopback".
It performs the operation of writing to a DO pin and reading from a DI pin.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
pin_state = [1, 0, 1, 0, 1, 0, 1]

## Write port to high or low
status = pywpc.DO_writePort(pin_state)
print("DO_writePort status: ", status)

## Read DI port state
state_list = pywpc.DI_readPort()
print("DI_readPort: ", state_list)
