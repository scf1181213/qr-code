#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time



def Switch(select):
    switch=40
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switch,GPIO.OUT,initial=GPIO.HIGH)
    if select==1:
        GPIO.output(switch,True)
        print "1"
    elif select==2:
        GPIO.output(switch,False)
        print "2"
    elif select==3:
        GPIO.cleanup(switch)








     
