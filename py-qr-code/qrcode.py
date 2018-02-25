#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import os , signal,subprocess

qrstr1="qrcode"
def qrtext():                                                                           #generate QRcode text
    text=raw_input(u"enter text QRcode:")                     #input QRcode text
    os.system("qrencode -o /home/scf/py-qr-code/createQR/"+qrstr1+".png '"+text+"'") #generate QRcode text
    print u"qrcode  in:"+qrstr1+".png"


def  distinguish():
    os.system("raspistill -w  320 -h 240 -o /home/scf/py-qr-code/QRimage/image.jpg")
    print u"raspistill finished"
    #child thread processing QRcode
    qrcamera=subprocess.Popen("zbarimg --raw /home/scf/py-qr-code/QRimage/image.jpg",stdout=subprocess.PIPE,shell=True,preexec_fn=os.setsid)
    qrcodetext=qrcamera.stdout.readline()
    if qrcodetext!="":
        print qrcodetext
    else:
        print u"qrcodetext is empty"
    return qrcodetext
    
    
    
    
