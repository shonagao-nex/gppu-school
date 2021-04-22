import sys
import time
import pigpio
from multiprocessing import Pool

interval = 0.001

pi = pigpio.pi()
pi.set_mode(5,pigpio.OUTPUT)
pi.set_mode(12,pigpio.OUTPUT)
pi.set_mode(13,pigpio.OUTPUT)
#pi.set_mode(14,pigpio.OUTPUT)
pi.set_mode(6,pigpio.OUTPUT)
pi.set_mode(16,pigpio.OUTPUT)
#pi.set_mode(17,pigpio.OUTPUT)
pi.set_mode(18,pigpio.OUTPUT)
#pi.set_mode(19,pigpio.OUTPUT)
#pi.set_mode(20,pigpio.OUTPUT)
pi.set_mode(21,pigpio.OUTPUT)
#pi.set_mode(22,pigpio.OUTPUT)
pi.set_mode(23,pigpio.OUTPUT)
pi.set_mode(24,pigpio.OUTPUT)
pi.set_mode(25,pigpio.OUTPUT)
pi.set_mode(26,pigpio.OUTPUT)

pi.write(5,1)
pi.write(12,1)
pi.write(16,1)
pi.write(18,1)

def getHz():
    file = open('count.txt','r')
    lines = file.readlines()
    n = lines[len(lines)-1]
    lst = []
    str_hz = str(n)
    if len(str_hz)>5:
        str_hz = str_hz[-5:-1] + '\n'
    space = 5 - len(str_hz)
    for i in range(space):
        lst.append(' ')
    for i in str_hz:
        lst.append(i)
    lst.pop(-1)
    return lst

def OnOff(ch,num):
    if num == 0:
        pi.write(ch,0)
    else:
        pi.write(ch,1)

def LEDoperation(number, cnt):
    seg = (24,26,23,13,6,21,25)
    dig = (5,12,16,18)
    num = {' ':(0,0,0,0,0,0,0),
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
    # num = {'':(0,0,0,0,0,0,0),
    #         '0':(1,1,1,1,1,1,1),
    #         '1':(1,1,1,1,1,1,1),
    #         '2':(1,1,1,1,1,1,1),
    #         '3':(1,1,1,1,1,1,1),
    #         '4':(1,1,1,1,1,1,1),
    #         '5':(1,1,1,1,1,1,1),
    #         '6':(1,1,1,1,1,1,1),
    #         '7':(1,1,1,1,1,1,1),
    #         '8':(1,1,1,1,1,1,1),
    #         '9':(1,1,1,1,1,1,1)}

    OnOff(dig[cnt-1],1)
    for i in range(0,7):
        OnOff(seg[i],num[number][i])
    OnOff(dig[cnt],0)

try:
    while True:
        lst = getHz()
        #print(lst)
        count = 0
        for nm in lst:
            LEDoperation(nm,count)
            count+=1
            time.sleep(interval)

except KeyboardInterrupt:
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

