'''
Modbus_master - write_coil.py.

""" Write single coil to the slave device.. """

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

host_ip = ""
salve_id = 1
address = 0
value = True

## Open Modbus master in background
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write 1 bits in modbus address 0
status = pywpc.ModbusMaster_writeCoil(address, int(value))

print(status)

## Close Modbus master in background
pywpc.ModbusMaster_close()
