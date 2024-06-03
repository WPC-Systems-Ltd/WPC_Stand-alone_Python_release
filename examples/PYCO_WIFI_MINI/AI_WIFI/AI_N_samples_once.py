'''
AI - AI_N_samples_once.py.

This example demonstrates how to read AI data in N-sample mode.

To begin with, it start AI acquisition with sampling rate and samples.
Then, it outlines the procedure for reading the streaming AI data.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
sampling_rate = 1000
sample = 10
delay = 2000

## Start AI acquisition
pywpc.AI_start(sampling_rate, sample)

## Read data acquisition
ai_sample = pywpc.AI_readNsample(sample, delay)
print(ai_sample)

## Stop AI acquisition
pywpc.AI_stop()

del ai_sample
