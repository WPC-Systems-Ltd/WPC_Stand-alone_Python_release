'''
Modbus_master - write_multi_registers.py.

""" Write the contents of two analog output holding registers to the slave device."""

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
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
