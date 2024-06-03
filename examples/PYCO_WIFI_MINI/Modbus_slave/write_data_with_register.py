'''
Modbus_slave - write_data_with_register.py.

This example demonstrates how to write data into slave

The range of input registers is from 41000 to 41499.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Open Modbus slave in background
pywpc.ModbusSlave_open()

## Write int value in Modbus slave's map
pywpc.ModbusSlave_inputRegisterWriteInt(41000, 5566)

## Write float value in Modbus slave's map
pywpc.ModbusSlave_inputRegisterWriteFloat(41002, 0.1234)

## Close Modbus slave in background
# pywpc.ModbusSlave_close()
