
'''
System - not_execute_main_py.py.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Prevent main.py from running automatically after reboot.
pywpc.Sys_disableMain()

## Reboot PYCO
pywpc.Sys_reboot()

