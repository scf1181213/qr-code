#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time



switch=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch,GPIO.OUT,initial=GPIO.LOW)
print (GPIO.getmode())
while True:
    select=int(raw_input(u"choose:"))
    if select==1:
        GPIO.output(switch,True)
    elif select==2:
        GPIO.output(switch,False)
    elif select==3:
        GPIO.cleanup(switch)
    else:
        break
    








     
