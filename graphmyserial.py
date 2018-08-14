#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:40:45 2018

@author: Yeahia Sarker

"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter
import serial
from sys import exit

class helloserial:
    def __init__(self, controller, baudrate = 9600, timeout = 0):
        """ Initializing serial communication """
        self.controller = serial.Serial( port = '/dev/atty1', baudrate = baudrate, timeout = timeout)
        if self.controller.isOpen():
            print("Serial port is created")
        else:
            try:
                self.controller.open()
            except Exception:
                print("Could not create serial communication. Please check your port and try again")
                exit()
    def decoding_data( string ):
        """ Getting microcontroller data via serial communication """
        data = ""
        string = string.decode()
        for i in string: # this loop will exclude all special characters
            if "," in i:
                continue
            if "'" in i:
                continue
            if " " in i:
                continue
            if "[" in i:
                continue
            if "]" in i:
                continue
            data = data + i
        return data
    def get_data( self ):
        serialdata = self.controller.read()
        decoding_data( serialdata )
        #Enough for today