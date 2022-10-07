from machine import Pin, PWM
import utime

# PWMに指定
pwm = PWM(Pin(25,Pin.OUT))

pwm.freq(10)
duty = 80
pwm.duty_u16(int(65535*duty/100))

# 演習課題
# 時間の経過によって、光が自動で変わるようにしていきましょう。