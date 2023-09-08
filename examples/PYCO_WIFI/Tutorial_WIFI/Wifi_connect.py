'''
Tutorial - Wifi_connect.py.

This example project demonstrates how to connect Wifi.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

import network

def do_connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

do_connect('my_ssid', 'my_password')

