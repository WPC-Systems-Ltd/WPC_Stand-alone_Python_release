'''
AI - AI_on_demand_once.py.

This example demonstrates how to read AI data in on demand mode.

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