'''
Tutorial - thread_LED.py.

This example project demonstrates how to use two thread to read AI data and set LED value.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.

'''
## WPC
import pywpc

## Python
import time
import _thread

f_run = True

## Define LED thread
def LED_thread():
    while f_run:
        pywpc.LED_setBlue()
        time.sleep(0.5)
        pywpc.LED_setGreen()
        time.sleep(0.5)
        pywpc.LED_setRed()
        time.sleep(0.5)

## Start LED thread
_thread.start_new_thread(LED_thread, ())

## Delay 10 seconds
time.sleep(10)

## Change flag
f_run = False