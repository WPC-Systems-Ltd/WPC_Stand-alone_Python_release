'''
Modbus_master - write_multi_registers.py.

""" Write the contents of two analog output holding registers to the slave device."""

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

host_ip = ""
salve_id = 1
address = 0
value_list = [5566, 1234]

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write multi value in modbus address 0
status = pywpc.ModbusMaster_writeMultiRegisters(address, value_list)

print(status)

## Close Modbus master
pywpc.ModbusMaster_close()