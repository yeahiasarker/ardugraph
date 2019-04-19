#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:40:45 2018

@author: Yeahia Sarker

"""
import io
import json
import logging
import serial
import string
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter


class helloserial:
    def __init__(self, baudrate = 9600, timeout = 1):
        """ initializing serial communication """
        #self.logging.basicConfig(filename = "error.log", level = logging.INFO, format = '%(asctime)s:%(levelname)s:%(message)s')
        self.controller = serial.Serial( port = '/dev/ttyACM0', baudrate = baudrate, timeout = timeout)
        self.controller_io = io.TextIOWrapper(io.BufferedRWPair(self.controller, self.controller, 1),  
                               newline = '\r',
                               line_buffering = True)
        if self.controller.isOpen():
            #logging.INFO('serial communication has been established')
            print("serial communication has been established")
        else:
            try:
                self.controller.open()
            except Exception:
                #logging.ERROR("couldn't establish serial communication")
                #logging.ERROR("please check the port and baudrate")
                sys.exit()
    def logging_data(self):
        """ saving the arduino sensor information in a log file"""
        with open('sensor_data.log','w') as f:
            json.dump(self.read_continuous_data, f)
    def show_data():
        """ Loading json sensor data log file """
        
    def preprocessing_data(serial_data):
        """ data preprocessing """
        data = ""
        serial_data = serial_data.decode()
        printable = set(serial_data.printable) # Removing non-ascii characters
        filter(lambda x: x in printable, s)
        for i in s: # this loop will exclude all special characters
            data = data + i
        return data

    def read_continuous_data(self):
        while True:
            try:
                serial_data = self.controller_io.readline()
                print(serial_data)
                time.sleep(0.3)
            except Exception as e:
                print()
    
    def plot_data(self):
        """ Ploting data using matplotlib """
        
    def write_data():
        """ writing data to arduino """

man = helloserial()
man.read_continuous_data()
        
        
        #Enough for today
