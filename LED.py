from machine import Pin, PWM
import utime
import time

# PWMに指定
led = Pin(18,Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    
    led.value(0)
    time.sleep(1)
