'''
Button - read_function_button.py.

This example demonstrates how to read function button status

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc
import time

print("Start reading function button status")
while (pywpc.Sys_readFuncButton() == 1):
    time.sleep(1)
    print("Push FUNC button to leave loop")

print("End code")