'''
Tutorial - thread_LED.py.

This example project demonstrates how to use two thread to read AI data and set LED value.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Python
import time
import _thread

## Define AI thread
def AI_thread():
    while True:
        print(pywpc.AI_readOnDemand())
        time.sleep(0.5)

## Define LED thread
def LED_thread():
    while True:
        pywpc.LED_setBlue()
        time.sleep(0.5)
        pywpc.LED_setGreen()
        time.sleep(0.5)
        pywpc.LED_setRed()
        time.sleep(0.5)

# Start AI and LED thread
_thread.start_new_thread(AI_thread, ())
_thread.start_new_thread(LED_thread, ())
