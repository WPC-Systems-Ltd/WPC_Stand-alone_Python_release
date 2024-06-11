'''
SDCard - Read from SD Card.py.

This example demonstrates how to read from txt file.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

import pywpc_sd

## Initialize the SD card
dev = pywpc_sd.SDCard()

## Debug print SD card directory and files
print(dev.getFileDirectory())

## Open the file in "read mode".
## Read the file and print the text on debug port.
file = dev.openFile("sample.txt","r")

if file != 0:
    print("Reading from SD card")
    print (dev.readFile())

## Close the file
dev.closeFile()