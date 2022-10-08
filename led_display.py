import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c.scan())

import time
from esp8266_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
sda = machine.Pin(0)
scl = machine.Pin(1)

# I2C start
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.putstr("It Works!\nSecond Line")
time.sleep(3)
lcd.clear()
time.sleep(3)
lcd.putstr("Hello\nI'm METAELE")


# オヌヌメ
https://peppe8o.com/using-i2c-lcd-display-with-raspberry-pi-pico-and-micropython/



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
