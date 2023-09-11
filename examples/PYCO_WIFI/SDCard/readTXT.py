'''
SDCard - Read from SDCard.py.

This example demonstrates how to read from txt file.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

import sdcard
from machine import Pin, SPI
import os

## Initialize the SD card
sd_spi = SPI(1, sck = Pin(14, Pin.OUT), mosi = Pin(13, Pin.OUT), miso = Pin(12, Pin.OUT))

sd = sdcard.SDCard(sd_spi, Pin(15, Pin.OUT))

## Create a instance of MicroPython Unix-like Virtual File System (VFS)
vfs=os.VfsFat(sd)

## Mount the SD card
os.mount(sd,'/sd')

## Debug print SD card directory and files
print(os.listdir('/sd'))

## Open the file in "read mode".
## Read the file and print the text on debug port.
file = open("/sd/sample.txt", "r")
if file != 0:
    print("Reading from SD card")
    read_data = file.read()
    print (read_data)
## Close the file
file.close()