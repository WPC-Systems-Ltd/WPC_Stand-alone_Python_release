'''
DIO - DIO_loopback_pins.py.

This example shows how to use DIO loopback with port
It involves using DO pins to send signals and DI pins to receive signals on a single device, commonly known as "loopback".
It performs the operation of writing to a DO pin and reading from a DI pin.

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

## Read DI port state
state_list = pywpc.DO_readAllChannels()
print("DO_readAllChannels: ", state_list)