'''
Modbus_master - write_coil.py.

""" Write single coil to the slave device.. """

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
value = True

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Write 1 bits in modbus address 0
status = pywpc.ModbusMaster_writeCoil(address, int(value))

print(status)

## Close Modbus master
pywpc.ModbusMaster_close()