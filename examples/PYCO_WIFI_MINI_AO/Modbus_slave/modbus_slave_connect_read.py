'''
Modbus_slave - modbus_slave_connect_read.py.

This example demonstrates how to establish and manage a connection for a Modbus TCP Slave device, and then periodically read its internal data registers once a Modbus Master client connects.

The range of Holding Registers is from 40001 to 40500

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

## WPC
import pywpc

## Python
import time

# --- Modbus Configuration ---
START_ADDRESS = 40001 ## Assume Modbus Holding Registers start at 40001
NUM_REGISTERS = 10 ## Assume we want to read 10 registers (40001 to 40010)
READ_INTERVAL = 1.0 ## Time interval for periodic data reading (seconds)
CONNECTION_TIMEOUT = 20 ## Timeout for checking connection status (seconds)

def run_modbus_slave_example():
    ## Open Modbus Slave TCP server
    status = pywpc.ModbusSlave_open()
    if status != 0:
        print("Failed to open Modbus Slave TCP server. Please try again.")
        return

    ## Wait for master connection
    print("Waiting for master connection...")
    start_time = time.time()
    is_connected = False

    while time.time() - start_time < CONNECTION_TIMEOUT:
        connect_status = pywpc.ModbusSlave_getConnectStatus()

        if connect_status == 1:
            print("Connection successful!")
            is_connected = True
            break
        time.sleep(0.5) # Check every 0.5s

    if not is_connected:
        print(f"Connection failed after {CONNECTION_TIMEOUT} seconds timeout.")

    ## Read Holding Registers periodically
    try:
        while True:
            # Check current connection status
            connect_status = pywpc.ModbusSlave_getConnectStatus()
            if connect_status != 1:
                print("Client disconnected. Exiting read loop.")
                break

            ## Get holding register map
            register_data = pywpc.ModbusSlave_getHoldingRegisterMap(START_ADDRESS, NUM_REGISTERS)
            print(f"Holding register data: {register_data}")

            time.sleep(READ_INTERVAL)

    except KeyboardInterrupt:
        print("Keyboard interrupt detected.")

    finally:
        pywpc.ModbusSlave_close()

if __name__ == "__main__":
    run_modbus_slave_example()