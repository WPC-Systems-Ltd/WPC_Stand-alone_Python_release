'''
OLED - OLED_writeLine.py.

This example demonstrates how to write message on the screen.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Erase all message on the screen
pywpc.OLED_erase()

## Write in line 1
pywpc.OLED_writeLine("WPC Systems Ltd.", 1)

## Write in line 2
pywpc.OLED_writeLine("ChungleePeople", 2)

## Write in line 3
pywpc.OLED_writeLine("LincPeople", 3)

## Write in line 4
pywpc.OLED_writeLine("JustinPeople", 4)
