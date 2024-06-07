'''
TinyML - Movement classification.py.

This example demonstrates how to detect the acceleration of movement from time-series data.

In data read function, you should sequentially put acceleration X, acceleration Y, acceleration Z, gyro Y and gyro Z data in it.
Then, It will predict three situation, which is X-move, Y-move and circle-move.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## Standard
import gc
import time
import os
import machine
from machine import Timer
from ucollections import deque

## TinyML
from tinyml.config import config
from tinyml.data import Data
from tinyml.model import random_forest_a8c9ff5 as rf

## WPC
import pywpc

def read(t):
    '''Read AI data.'''
    ai_data = pywpc.AI_readOnDemand()
    data.collect([ai_data[0], ai_data[1], ai_data[2]], [ai_data[3], ai_data[4]])

def score(t):
    '''Runs scoring on collected data.'''
    gc.collect()
    input_data = data.data

    if len(input_data) == data_cap:
        res = rf.run(data.data)
        if res == 1:
            state = "x"
        elif res == 2 :
            state = "y"
        elif res == 3 :
            state = "circle"
        else:
            state = "no"
        print(f"Sending move: pred: { res}, type: { state} move")

def read_sensor():
    '''Timer to periodically read sensor values.'''
    Timer(0).init(freq=config.READ_SENSOR_FREQ,
                  mode=Timer.PERIODIC,
                  callback=read)

def run_score():
    '''Timer to periodically run scoring on collected data.'''
    Timer(1).init(freq=config.RUN_SCORE_FREQ,
                  mode=Timer.PERIODIC,
                  callback=score)

## Initialize data store
data = Data(freq=50, n_signals=5)
data_cap = data.capacity
print('[Main] Starting script')
print('[Main] Data store initiated. Capacity: {}\n\n'.format(data_cap))

## Read sensor
read_sensor()

## Run score
run_score()