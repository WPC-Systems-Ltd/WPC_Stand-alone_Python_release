'''
TinyML - predict_acceleration.py.

This example demonstrates how to detect the acceleration or the rotation of movement from time-series data.

The read_and_predict function uses measured acceleration and orientation to predict the movement.
Then, It will predict four situation:
-which is X_acc, Y_acc,  Z_acc and No Predicted Acceleration.
The output is the Led, which will be RED for X_acc, GREEN for Y_acc and BLUE for Z_acc.

For other examples please check:
    https://github.com/WPC-Systems-Ltd/WPC_Stand-alone_Python_release/tree/main/examples

Copyright (c) 2024 WPC Systems Ltd.
All rights reserved.
'''

## Standard
import time
from ulab import numpy as np

## WPC
import pywpc

## TinyML
from test_tree_acc import WPC_test_acceleration_tree

## Parameters
DR = np.pi / 180

class Queue:
    '''First In, First Out - FIFO'''
    def __init__(self, n):
        self.list = np.zeros(n)
        self.size = n
        self.head = 0

    def add(self, item):
        self.list[self.head] = item
        self.head = (self.head + 1) % self.size

def most_frequent_element(list, return_max_freq = False):
    '''Returns most frequent element of a list, and optionally, the frequency of this element'''
    if not list:  # For the case of an empty list
        return (None, 0) if return_max_freq else None
    most_freq_el = list[0]
    max_freq = 1
    h =  {}
    for items in list:
        if items not in h:
            h[items] = 1
        else:
            h[items] += 1

        if h[items] > max_freq:
            max_freq = h[items]
            most_freq_el = items
    if return_max_freq:
        return most_freq_el, max_freq
    return most_freq_el

def initialization(model):
    '''defines all the variables for prediction'''
    global data_acc, data_paste_gyr, data_current_gyr, data_diff_gyr, pred_acc, pred_gyr, wide_tab, MODEL, MAP, MAP_LED
    data_acc = np.zeros(3)

    data_past_gyr = np.zeros(3)
    data_current_gyr = np.zeros(3)
    data_diff_gyr = data_current_gyr - data_past_gyr

    pred_acc = Queue(7)
    pred_gyr = Queue(7)

    '''wide_tab is the "concatenation" of seven current tabs, 6x7 = 42, hence a such result'''
    wide_tab = np.zeros(42)

    MODEL = model

    MAP_LED = {0: pywpc.LED_reset, 1: pywpc.LED_setGreen, 2: pywpc.LED_setBlue, 3: pywpc.LED_setRed}

def read_and_predict(g):
    '''it reads the current data, and predicts the movement based on the last 7 data read'''
    global data_acc, data_current_gyr, data_diff_gyr, wide_tab
    t0 = time.ticks_ms()

    '''Read AI data.'''
    data_past_gyr = data_current_gyr
    data_current_gyr = np.array(pywpc.AHRS_getOrientation())
    data_diff_gyr = data_current_gyr - data_past_gyr

    '''remove the gravity component'''
    data_acc = np.array(pywpc.AHRS_getAcceleration()) - 9.81*np.array([np.sin(DR*data_current_gyr[1]),
                                                np.sin(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1]),
                                                np.cos(DR*data_current_gyr[0])*np.cos(DR*data_current_gyr[1])])

    wide_tab = np.concatenate((data_acc, data_diff_gyr, wide_tab[:-6]))

    pred = MODEL(wide_tab)

    return pred

def main():
    '''predicts movement for 10 iterations, and return the most frequent prediction'''
    pywpc.AHRS_start()
    pywpc.LED_reset()
    initialization(model = WPC_test_acceleration_tree)
    time.sleep(1)

    preds = Queue(10)
    start = time.ticks_ms()
    while True:
        preds.add(read_and_predict(0))
        time.sleep_ms(45)
        end = time.ticks_ms()
        print(time.ticks_diff(end, start))
        start = time.ticks_ms()
        '''X_acc: RED ; Y_acc: GREEN ; Z_acc: RED, No Acceleration Detected: No Color'''
        MAP_LED[most_frequent_element(preds.list)]()
    pywpc.AHRS_stop()
print('[Main] Starting script')

main()