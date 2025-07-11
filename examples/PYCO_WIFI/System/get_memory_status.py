
'''
System - get_memory_status.py.

This example project shows how to get RAM and flash memory.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Python
import time
import gc
import os

def WPC_getFlashInfo():
  s = os.statvfs('//')
  return ('Flash size: {0} MB'.format((s[0]*s[3])/1048576))

def WPC_getRAMInfo():
  F = gc.mem_free()
  A = gc.mem_alloc()
  T = F+A
  P = '{0:.2f}%'.format(F/T*100)
  return ('Total SRAM: {0} MB, Free SRAM: {1} MB ({2})'.format((T/1048576), (F/1048576), P))

print(WPC_getFlashInfo())
print(WPC_getRAMInfo())
