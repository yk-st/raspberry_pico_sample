from machine import Pin
import utime

# gpio 設定
pir = Pin(1, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

led.value(0)
utime.sleep(5)

# 監視の開始
while True:
    print(pir.value())
    if pir.value() == 0:
        led.value(0)
        utime.sleep(1)
    else:
        led.value(1)
        utime.sleep(6)