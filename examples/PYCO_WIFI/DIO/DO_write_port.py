'''
DIO - DO_write_pins.py.

This example shows how to write high or low signal to DO port.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
pin_state = [1, 0, 1, 0, 1, 0, 1]

## Write port to high or low
status = pywpc.DO_writeAllChannels(pin_state)
print("DO_writeAllChannels status: ", status)