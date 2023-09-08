'''
FFT - fourier_transform_simulate.py.

This example demonstrates how to use fourier transform with AI N-sample data

Copyright (c) 2023 WPC Systems Ltd. All rights reserved.
'''

from ulab import numpy as np
import pywpc

## Parameters
sampling_rate = 1000
sample = 1024
delay = 2000

## Start AI acquisition
pywpc.AI_start(sampling_rate, sample)

## Read data acquisition
ai_sample = pywpc.AI_readNsample(sample, delay)

## Convert AI data
ai_sample_cvt = [list(i) for i in zip(*ai_sample)]

## Convert from list to array
ai_sample_cvt_arr = np.array(ai_sample_cvt)

## Apply the FFT on the signal
## Get channel 1 data
fourier_real, fourier_imaginary = np.fft.fft(ai_sample_cvt_arr[1])
power_spectrum = fourier_real**2 + fourier_imaginary**2

## Print result
print(power_spectrum)
print(len(power_spectrum))
print(max(power_spectrum))