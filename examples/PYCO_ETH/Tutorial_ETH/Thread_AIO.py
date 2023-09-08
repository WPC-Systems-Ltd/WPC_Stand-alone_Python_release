'''
Tutorial - Thread_AIO.py with asynchronous mode.

This example project demonstrates how to use thread to get RTC from EthanO.

-------------------------------------------------------------------------------------
Please change correct serial number or IP and port number BEFORE you run example code.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Python_driver_release/tree/main/examples
See README.md file to get detailed usage of this example.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## import
import pywpc
import time
import _thread
import random

## Define AI thread
def AI_thread():
    while True:
        print(pywpc.AI_readOnDemand())
        time.sleep(1)

## Define AO thread
def AO_thread():
    while True:
        channel = random.randint(0, 7)     ## Channel   0~7
        ao_value = random.randint(-10, 10) ## Voltage -10~10
        pywpc.AO_writeOneChannel(channel, ao_value)
        print(f'Set channel {channel} to {ao_value}V')
        time.sleep(5)

## Start AI and AO thread
_thread.start_new_thread(AI_thread, ())
_thread.start_new_thread(AO_thread, ())
