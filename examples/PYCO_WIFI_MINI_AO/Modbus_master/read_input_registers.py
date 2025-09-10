'''
Modbus_master - read_input_registers.py.

""" Read 10 input registers from the slave device. """

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
registers = 10

## Open Modbus master
pywpc.ModbusMaster_open(host_ip, salve_id)

## Read 10 registers at address 0, store result in regs list
regs_l = pywpc.ModbusMaster_readInputRegister(address, registers)

print(regs_l)

## Close Modbus master
pywpc.ModbusMaster_close()