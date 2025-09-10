'''
FFT - fourier_transform_simulate.py.

This example demonstrates how to use fourier transform with simulated data

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2025 WPC Systems Ltd.
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

## Square signal
# signal = [1.0 if (frequency*x % 1) < 0.5 else -1.0 for x in t]
# signal = np.array(signal)

## Apply the FFT on the signal
fourier_real, fourier_imaginary = np.fft.fft(signal)
power_spectrum = fourier_real**2 + fourier_imaginary**2

## Print result
print(power_spectrum)
print(len(power_spectrum))
print(max(power_spectrum))