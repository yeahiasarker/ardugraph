#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:40:45 2018

@author: Yeahia Sarker

"""

import json
import logging
import serial
import string
from sys import exit
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter


class helloserial:
    def __init__(self, controller, baudrate = 9600, timeout = 0):
        """ initializing serial communication """
        self.logging.basicConfig(filename = "error.log", level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')
        self.controller = serial.Serial( port = '/dev/atty1', baudrate = baudrate, timeout = timeout)
        if self.controller.isOpen():
            logging.INFO('serial communication has been established')
        else:
            try:
                self.controller.open()
            except Exception:
                logging.ERROR("couldn't establish serial communication")
                logging.ERROR("please check the port and baudrate")
                exit()
    def logging_data():
        """ saving the arduino sensor information in a log file"""
        with open('sensor_data.log','w') as f:
            json.dump(get_data, f)
        
    def preprocessing_data(strin):
        """ data preprocessing """
        data = ""
        strin = strin.decode()
        printable = set(string.printable) # Removing non-ascii characters
        filter(lambda x: x in printable, s)
        for i in x: # this loop will exclude all special characters
            data = data + i
        return data

    def get_data(self):
        serial_data = self.controller.read()
        final_data = preprocessing_data(serial_data)
        return final_data
        
        #Enough for today
