# no AD converter1
# ラズパイ picoはADが内蔵しているのでそのまま使える
from machine import ADC, Pin

a = ADC(2)
coeff = 3.3/ 65535

#  アナログデータをデジタルデータに変換する
v = a.read_u16()*coeff
print(v)

led = Pin(16, Pin.OUT)

led.value(1)

# PMWと合わせて光の強さを調節してみよう