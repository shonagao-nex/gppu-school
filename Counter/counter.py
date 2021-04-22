#!/usr/bin/python
import pigpio
import time

interval = 10
count = 0
hz = 0

pi = pigpio.pi()
pi.set_mode(17, pigpio.INPUT)
pi.set_pull_up_down(17, pigpio.PUD_UP)

def cb_interrupt(gpio, level, tick):
    global count
    count = count+1
    #print(gpio, count)

cb = pi.callback(17, pigpio.FALLING_EDGE, cb_interrupt)

try:
    while(True):
        time.sleep(interval)
        #hz = count/interval
        hz = count
        file = open('count.txt','a')
        file.write('%.lf\n' %hz )
        file.close()
        hz = 0
        count = 0
        
        
except KeyboardInterrupt:
    print("break")
