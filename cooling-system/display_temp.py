#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from time import sleep
from re import findall

def get_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)

while True:
    temp = get_temp()
    print(temp)
    sleep(1)     