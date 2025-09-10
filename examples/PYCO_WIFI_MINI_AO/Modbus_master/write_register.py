'''
Modbus_master - write_register.py.

""" Write single coils to the slave device. """

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
value = 5566

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write `5566` in modbus address 0
status = pywpc.ModbusMaster_writeRegister(address, value)

print(status)

## Close Modbus master
pywpc.ModbusMaster_close()