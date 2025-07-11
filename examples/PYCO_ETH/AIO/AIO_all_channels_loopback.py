'''
AIO - AIO_all_channels_loopback.py.

This example demonstrates the process of AIO loopback across all channels.
It involves using AO pins to send signals and AI pins to receive signals on a single device, commonly referred to as "loopback".
The AI and AO pins are connected using a wire.
The AO range is -10 to 10 V.

First, it reads AI data and displays its corresponding values.
Following that, it writes digital signals to the AO pins and reads AI on demand data once again.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Read data acquisition
ai_data = pywpc.AI_readOnDemand()
print(ai_data)

## Write AO value simultaneously
voltage_list = [-10, -7.5, -5, -2.5, 3.5, 5.5, 7.5, 10]
status = pywpc.AO_writeAllChannels(voltage_list)
print("AO_writeAllChannels status: ", status)

## Read data acquisition
ai_data = pywpc.AI_readOnDemand()
print(ai_data)