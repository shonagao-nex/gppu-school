import time
import pigpio

pi = pigpio.pi()                  # call pigpio
pi.set_mode(10,pigpio.OUTPUT)     # set GPIO10 to Output

print("type Ctrl-C to finish this macro")

interval = 0.5                    # interval time LED blinking

try:
    while True:
        pi.write(10,1)            # turn on
        time.sleep(interval)
        pi.write(10,0)            # turn off
        time.sleep(interval)
except KeyboardInterrupt:         # turn of with Ctrl+C
    pi.write(10,0)

