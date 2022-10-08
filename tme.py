import machine
import time

mcp9700 = machine.ADC(0)

while True:
    value = mcp9700.read_u16()
    volt = value / 65535 * 3.3
    temp = volt * 100 - 50
    print(temp)
    time.sleep(1)

from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

while True:
    time.sleep(5)
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
