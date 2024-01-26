'''
Modbus_master - read_coils.py.

""" Read 10 coils from the slave device. """

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

host_ip = ""
salve_id = 1
address = 0
coils = 10

## Open Modbus master in background
pywpc.ModbusMaster_open(host_ip, salve_id)

## Read 10 bits (= coils) at address 0, store result in coils list
coils_l = pywpc.ModbusMaster_readCoils(address, coils)

print(coils_l)

## Close Modbus master in background
pywpc.ModbusMaster_close()
