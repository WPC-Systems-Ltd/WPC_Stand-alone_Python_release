'''
LED - LED_control.py.

This example demonstrates how to control LED.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
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
