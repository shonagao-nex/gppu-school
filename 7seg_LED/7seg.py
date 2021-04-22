##################################################################
# This is a macro file for 4-digit 7-seg LED operation.          #
# clock                                                          #
# execution: python3 7seg.py                                     #
# S.Nagao                                                        #
##################################################################
import sys
import time
import pigpio
from multiprocessing import Pool

interval = 0.001

pi = pigpio.pi()
pi.set_mode(5,pigpio.OUTPUT)    # 4th digit
pi.set_mode(12,pigpio.OUTPUT)   # 3rd digit
pi.set_mode(13,pigpio.OUTPUT)   # D
#pi.set_mode(14,pigpio.OUTPUT)   # Dot
pi.set_mode(6,pigpio.OUTPUT)    # E
pi.set_mode(16,pigpio.OUTPUT)   # 2nd digit
#pi.set_mode(17,pigpio.OUTPUT)   # Dot
pi.set_mode(18,pigpio.OUTPUT)   # 1st digit
#pi.set_mode(19,pigpio.OUTPUT)   # Dot
#pi.set_mode(20,pigpio.OUTPUT)   # Dot
pi.set_mode(21,pigpio.OUTPUT)   # F
#pi.set_mode(22,pigpio.OUTPUT)   # Dot
pi.set_mode(23,pigpio.OUTPUT)   # C
pi.set_mode(24,pigpio.OUTPUT)   # A
pi.set_mode(25,pigpio.OUTPUT)   # G
pi.set_mode(26,pigpio.OUTPUT)   # B

# Set High-level (All digits off)
pi.write(5,1)
pi.write(12,1)
pi.write(16,1)
pi.write(18,1)

def getTime():
    n = time.strftime('%M') + time.strftime('%S')
    timeList = list(n)
    return timeList

def OnOff(ch,num):
    if num == 0:
        pi.write(ch,0)
    else:
        pi.write(ch,1)

def LEDoperation(number, cnt):
    seg = (24,26,23,13,6,21,25)   # A B C D E F G
    dig = (5,12,16,18)            # 4th 3rd 2nd 1st
    num = {'':(0,0,0,0,0,0,0),
            '0':(1,1,1,1,1,1,0),
            '1':(0,1,1,0,0,0,0),
            '2':(1,1,0,1,1,0,1),
            '3':(1,1,1,1,0,0,1),
            '4':(0,1,1,0,0,1,1),
            '5':(1,0,1,1,0,1,1),
            '6':(1,0,1,1,1,1,1),
            '7':(1,1,1,0,0,1,0),
            '8':(1,1,1,1,1,1,1),
            '9':(1,1,1,1,0,1,1)}

    OnOff(dig[cnt-1],1)               # select digit
    for i in range(0,7):              # make number
        OnOff(seg[i],num[number][i])
    OnOff(dig[cnt],0) 

try:
    while True:
        lst = getTime()
        count = 0
        for nm in lst:
            LEDoperation(nm,count)
            count+=1
            time.sleep(interval)
except KeyboardInterrupt:          # turn off all outputs with Ctrl+C
    pi.write(5,0)
    pi.write(12,0)
    pi.write(13,0)
#    pi.write(14,0)
    pi.write(6,0)
    pi.write(16,0)
#    pi.write(17,0)
    pi.write(18,0)
#    pi.write(19,0)
#    pi.write(20,0)
    pi.write(21,0)
#    pi.write(22,0)
    pi.write(23,0)
    pi.write(24,0)
    pi.write(25,0)
    pi.write(26,0)

