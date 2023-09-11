'''
SDCard - Write into SDCard.py.

This example demonstrates how to write messages into file.

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

## Create / Open a file in write mode.
## Write mode creates a new file.
## If already file exists. Then, it overwrites the file.
file = open("/sd/sample.txt","w")

## Write sample text
for i in range(20):
    file.write("Sample text = %s\r\n" % i)

## Close the file
file.close()