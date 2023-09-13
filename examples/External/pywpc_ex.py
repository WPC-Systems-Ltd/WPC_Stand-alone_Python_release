import sdcard
import os
from machine import Pin, SPI

class SDCard:
    def __init__(self):
         ## Initialize the SD card
        sd = sdcard.SDCard(SPI(1), Pin(15, Pin.OUT))
        os.mount(sd,'/sd')

    def getFiles(self):
        return os.listdir('/sd')

    def openFile(self, filename, mode):
        self.file = open(f'/sd/{filename}', mode)
        return self.file

    def writeFile(self, str_):
        self.file.write(str_)
