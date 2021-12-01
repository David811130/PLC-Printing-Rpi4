#!/usr/bin/python
import requests
import cups
import shutil
from urllib.request import urlretrieve
from datetime import date
import RPi.GPIO as GPIO
import time

#Pin Definitions:
ndPin = 40
pdPin = 38
rePin = 37
sePin = 35
tePin = 33
uePin = 31 

#Pin Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ndPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pdPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(tePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(uePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)





    
def labelND():
#dateformat: dd-mm-yy       
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("nd_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-ND^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-ND^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/nd_print.prn', '',{'fit-to-page':'True'})
    
    
def labelPD():
#dateformat: dd-mm-yy
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("pd_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-PD^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-PD^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/pd_print.prn', '',{'fit-to-page':'True'})
    
    
def labelRE():
#dateformat: dd-mm-yy
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("re_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-RE^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-RE^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/re_print.prn', '',{'fit-to-page':'True'})
    
    
def labelSE():
#dateformat: dd-mm-yy
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("se_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-SE^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-SE^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/se_print.prn', '',{'fit-to-page':'True'})
    
def labelTE():
#dateformat: dd-mm-yy
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("te_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-TE^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-TE^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/te_print.prn', '',{'fit-to-page':'True'})
    

def labelUE():
#dateformat: dd-mm-yy
    today = date.today()
    datestamp = today.strftime("%d/%m/%y")
    f = open("ue_print.prn","w+")
    f.write("^XA" + "\n"
        + "^SZ2^JMA" + "\n"
        + "^MCY^PMN" + "\n"
        + "^PW710" + "\n"
        + "~JSN" + "\n"
        + "^JZY" + "\n"
        + "^LH0,0^LRN" + "\n"
        + "^XZ" + "\n"
        + "^XA" + "\n"
        + "^FO26,27" + "\n"
        + "^BQN,2,6^FDLA,JB3C-5560-UE^FS" + "\n"
        + "^FT183,49" + "\n"
        + "^CI0" + "\n"
        + "^A0N,34,35^FDFoMoCo^FS" + "\n"
        + "^FT488,47" + "\n"
        + "^A0N,34,35^FD" + datestamp + "^FS" + "\n"
        + "^FT172,120" + "\n"
        + "^A0N,51,34^FDJB3C-5560-UE^FS" + "\n"
        + "^FT172,172" + "\n"
        + "^A0N,34,35^FDSOUTH AFRICA^FS" + "\n"
        + "^FT530,172" + "\n"
        + "^A0N,34,35^FDAVSHB^FS" + "\n"
        + "^FO172,14" + "\n"
        + "^GB136,45,3^FS" + "\n"
        + "^PQ1,0,1,Y" + "\n"
        + "^XZ")
    f.close()
    
    conn = cups.Connection()
    printers = conn.getPrinters()
    conn.printFile('Roan','/home/pi/ue_print.prn', '',{'fit-to-page':'True'})
    

def mainApp():
    ndState = GPIO.input(ndPin)
    pdState = GPIO.input(pdPin)
    reState = GPIO.input(rePin)
    seState = GPIO.input(sePin)
    teState = GPIO.input(tePin)
    ueState = GPIO.input(uePin)
    if(ndState == 1):
        print ("ND is HIGH")
        labelND()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    elif(pdState == 1):
        print ("PD is HIGH")
        labelPD()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    elif(reState == 1):
        print ("RE is HIGH")
        labelRE()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    elif(seState == 1):
        print ("SE is HIGH")
        labelSE()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    elif(teState == 1):
        print ("TE is HIGH")
        labelTE()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    elif(ueState == 1):
        print ("UE is HIGH")
        labelUE()
        time.sleep(1)
        print ("Checking for input in 5 seconds")
        time.sleep(5)
    else:
        print ("No valid input detected. Checking for input in: ")
        print ("5")
        time.sleep(1)
        print ("4")
        time.sleep(1)
        print ("3")
        time.sleep(1)
        print ("2")
        time.sleep(1)
        print ("1")
        time.sleep(1)
        

        
        


while True:
    try:
        mainApp()
        
    except Exception as ex:
        print(ex)
        mainApp()

#PROD_VER_3.0(NOV_2021)
