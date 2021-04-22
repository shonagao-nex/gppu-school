import sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=0.005)

ser.reset_input_buffer()

string = ('H:1') + '\r\n'
ser.write(string)
time.sleep(0.1)
res = ser.readline()
print(res)

ser.close()
