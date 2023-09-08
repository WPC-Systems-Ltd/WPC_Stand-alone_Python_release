'''
AI - AI_on_demand_once.py.

This example demonstrates how to read AI data in on demand mode.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Read data acquisition
ai_data = pywpc.AI_readOnDemand()
print(ai_data)
