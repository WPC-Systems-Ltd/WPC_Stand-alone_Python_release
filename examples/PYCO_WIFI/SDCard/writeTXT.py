'''
SDCard - Write to SD Card.py.

This example demonstrates how to write messages into file.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
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
    dev.writeFile("Sample text = %s\r\n" % i)

## Close the file
dev.closeFile()