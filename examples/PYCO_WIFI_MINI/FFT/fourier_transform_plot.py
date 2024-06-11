'''
FFT - fourier_transform.py.

This example demonstrates how to plot FFT signal
For PC relative plotting code, please refer https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/blob/main/examples/PC/TCP_client_with_plot_FFT.py

Step1: Generate FFT signal

Step2: Convert float to U8 list

Step3: Connect to Wifi

Step4: Send data via TCP server

Step5: Plot FFT signal in PC

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

from ulab import numpy as np
import pywpc

## Parameters
Fs = 256                ## sampling rate
Ts = 1.0/Fs             ## sampling interval
t = np.arange(0, 1, Ts) ## time vector
frequency = 50          ## frequency of the signal

## Sine signal
signal = np.sin(2*np.pi*frequency*t)

## Apply the FFT on the signal
fourier_real, fourier_imaginary = np.fft.fft(signal)
power_spectrum = fourier_real**2 + fourier_imaginary**2

## Create list
u8_list = []
for i in power_spectrum:
    u8_list.extend(pywpc.Sys_convertF32To4U8(i))

## Connect to Wifi

## Open TCP server
pywpc.TCPServer_open(5566)

## Send u8 list data
pywpc.TCPServer_writeU8List(u8_list)

## Close TCP server
pywpc.TCPServer_close()