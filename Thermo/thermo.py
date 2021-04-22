import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 0x03
spi.max_speed_hz = 5000
spi.xfer([0xFF, 0xFF, 0xFF, 0xFF])

try:
    while True:
        time.sleep(0.5)
        spi.xfer([0x54])
        time.sleep(1)

        ret = spi.xfer([0xFF, 0xFF])
        val = ret[0]<<8 | ret[1]
        val = val >> 3

        if(val >= 4096):
            val = val - 8192

        temp = val / 16.0

        print("temp: ",temp)
        file = open('thermo.txt','a')
        file.write('%.2lf\n' % temp)
        file.close()

except KeyboardInterrupt:
    spi.close()
