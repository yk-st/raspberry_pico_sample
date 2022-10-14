from machine import Pin,PWM

import time 


pwma_PIN = 2

AI1_PIN = 3

AI2_PIN = 4


mota1 = Pin(AI1_PIN, Pin.OUT)

mota2 = Pin(AI2_PIN, Pin.OUT)

pwma = PWM(Pin(pwma_PIN))


pwma.freq(1000)

duty=50

 
while True:

   

    #foward(正転)

    mota1.value(1)

    mota2.value(0)

    duty_16 = int((duty*65536)/100)

    pwma.duty_u16(duty_16)

    time.sleep(5)


    #coast(空転)

    mota1.value(0)

    mota2.value(0)

    duty_16 = int((duty*65536)/100)

    pwma.duty_u16(duty_16)

    time.sleep(5)

    

    #reverse(逆転)

    mota1.value(0)

    mota2.value(1)

    duty_16 = int((duty*65536)/100)

    pwma.duty_u16(duty_16)

    time.sleep(5)

    

    #brake

    mota1.value(1)

    mota2.value(1)

    duty_16 = int((duty*65536)/100)

    pwma.duty_u16(duty_16)

    time.sleep(5)


