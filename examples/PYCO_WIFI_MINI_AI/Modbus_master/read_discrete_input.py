'''
Modbus_master - read_discrete_input.py.

""" Read discrete input from the slave device. """

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
coils = 10

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Read 10 bits (= coils) at address 0, store result in coils list
coils_l = pywpc.ModbusMaster_readDiscreteInputs(address, coils)

print(coils_l)

## Close Modbus master
pywpc.ModbusMaster_close()