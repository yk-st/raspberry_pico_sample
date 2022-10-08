from machine import Pin, PWM
import utime
import time

# PWMに指定
sw = Pin(15,Pin.IN, Pin.PULL_DOWN)
led = Pin(18,Pin.OUT)

while True:
    print(sw.value())
    if (sw.value() == 1):
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.5)
