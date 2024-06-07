'''
LED - LED_control.py.

This example demonstrates how to control LED.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc
import time

## Reset LED
pywpc.LED_reset()

## Set LED to blue
pywpc.LED_setBlue()
time.sleep(0.5)

## Set LED to green
pywpc.LED_setGreen()
time.sleep(0.5)

## Set LED to red
pywpc.LED_setRed()