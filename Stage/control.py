import sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.005)

ser.reset_input_buffer()

string = ('Q:') + '\r\n'
ser.write(string)
time.sleep(0.010)
res = ser.readline()
print('Initial Position: ' + res)

string = ('A:1+P40000') + '\r\n'
ser.write(string)
time.sleep(0.1)
res = ser.readline()

string = ('G:') + '\r\n'
ser.write(string)
time.sleep(0.5)
res = ser.readline()
print('Start moving')
time.sleep(1)

string = ('Q:') + '\r\n'
ser.write(string)
time.sleep(0.01)
res = ser.readline()
print('New Position: ' + res)


ser.close()
