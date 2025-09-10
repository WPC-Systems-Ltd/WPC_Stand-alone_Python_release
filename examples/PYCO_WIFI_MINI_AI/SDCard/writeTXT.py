'''
SDCard - Write to SD Card.py.

This example demonstrates how to write messages into file.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
All rights reserved.
'''

import pywpc_sd

## Initialize the SD card
dev = pywpc_sd.SDCard()

## Debug print SD card directory and files
print(dev.getFileDirectory())

## Create / Open a file in write mode.
## Write mode creates a new file.
## If already file exists. Then, it overwrites the file.
dev.openFile("sample.txt","w")

## Write sample text
for i in range(20):
    dev.writeStringToFile("Sample text = %s\r\n" % i)

## Close the file
dev.closeFile()