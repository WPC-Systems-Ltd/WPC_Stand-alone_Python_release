'''
AI - AI_N_samples_with_logger.py.

This example demonstrates how to read AI data in N-sample mode and save it into a CSV file.

To begin with, it start AI acquisition with sampling rate and samples.
Then, it outlines the procedure for reading the streaming AI data.
Last, save the AI data to CSV file.

Copyright (c) 2023-2024 WPC Systems Ltd. All rights reserved.
'''

## WPC
import pywpc

## Parameters setting
sampling_rate = 8000
sample = 10000
delay = 2000

## Start AI acquisition
pywpc.AI_start(sampling_rate, sample)

## Read data acquisition
ai_sample = pywpc.AI_readNsample(sample, delay)
ai_len = len(ai_sample)

## Stop AI acquisition
pywpc.AI_stop()

## Open CSV file
ai_file = open("AI_test.csv", 'w')

## Write CSV file
ai_file.write("ch0,ch1,ch2,ch3,ch4,ch5,ch6,ch7\r\n")
for i in range(ai_len):
    res = ','.join(map(str, ai_sample[i]))
    ai_file.write(res+'\r\n')

## Close CSV file
ai_file.close()

del ai_sample
