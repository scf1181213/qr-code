#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import qrcode
import switch
from time import sleep
import py_sql
import RPi.GPIO as GPIO
import time

switch=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch,GPIO.OUT,initial=GPIO.LOW)
print (GPIO.getmode())

while(True):
    cur=py_sql.connection()
    res=py_sql.getkey(cur)
    print res[0][0]

    result=qrcode.distinguish().strip()
    print result
    if res[0][0]==result:
        GPIO.output(switch,False)
    sleep(5)
    GPIO.output(switch,True)
   
