'''
Modbus_master - write_multi_coils.py.

""" Write a series of 10 discrete coils to the slave device."""

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

host_ip = ""
salve_id = 1
address = 0
coil_list = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write multi bits in modbus address 0
status = pywpc.ModbusMaster_writeMultiCoils(address, coil_list)

print(status)

## Close Modbus master
pywpc.ModbusMaster_close()
