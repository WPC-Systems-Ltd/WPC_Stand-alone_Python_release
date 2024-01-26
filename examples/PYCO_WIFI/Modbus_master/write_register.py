'''
Modbus_master - write_register.py.

""" Write single coils to the slave device. """

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

host_ip = ""
salve_id = 1
address = 0
value = 5566

## Open Modbus master in background
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write `5566` in modbus address 0
status = pywpc.ModbusMaster_writeRegister(address, value)

print(status)

## Close Modbus master in background
pywpc.ModbusMaster_close()
