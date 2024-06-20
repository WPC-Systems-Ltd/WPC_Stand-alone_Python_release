
'''
System - get_memory_status.py.

This example project shows how to get flash memory.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.

'''

## WPC
import pywpc

flash_size = pywpc.Sys_getFlashSize()
print(flash_size)
