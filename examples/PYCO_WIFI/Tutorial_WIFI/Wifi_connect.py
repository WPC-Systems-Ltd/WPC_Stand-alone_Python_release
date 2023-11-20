'''
Tutorial - Wifi_connect.py.

This example project demonstrates how to connect Wifi.

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

import network

TRY_TIMES = 50

def do_connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        try_times = 0
        while not sta_if.isconnected() and try_times < TRY_TIMES:
            try_times+=1
            pass
    print('Network config:', sta_if.ifconfig())

do_connect('my_ssid', 'my_password')

