# オヌヌメ
https://peppe8o.com/using-i2c-lcd-display-with-raspberry-pi-pico-and-micropython/


# import machine
# sdaPIN=machine.Pin(0)
# sclPIN=machine.Pin(1)
# i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
# devices = i2c.scan()
# if len(devices) == 0:
#  print("No i2c device !")
# else:
#  print('i2c devices found:',len(devices))
# for device in devices:
#  print("Hexa address: ",hex(device))


from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

while True:
    
    lcd.putstr("Hello\nI'm METAELE")
    time.sleep(1)
    lcd.clear()
