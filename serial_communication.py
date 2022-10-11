from machine import Pin, I2C, UART
from utime import sleep
import ustruct

#unsignedを、signedに変換(16ビット限定）
def u2s(unsigneddata):
    if unsigneddata & (0x01 << 15) : 
        return -1 * ((unsigneddata ^ 0xffff) + 1)
    return unsigneddata

class mpu6050:
    def __init__(self, scl, sda):
        self.scl = scl
        self.sda = sda
        self.i2c = I2C(0,scl = self.scl, sda = self.sda, freq = 100000)
        slv = self.i2c.scan()
        self.slvAddr = slv[0] #slv[0]
        # レジスタをリセットする
        self.writeByte(0x6B,0x80) 
        sleep(0.1)     

        # PWR_MGMT_1をクリア
        self.writeByte(0x6B,0x00) 
        sleep(0.1)

    def readXYZ(self):
        data    = self.readByte(0x3B ,6)
        x    = (2.0 / 0x8000) * u2s(data[0] << 8 | data[1])
        y    = (2.0 / 0x8000) * u2s(data[2] << 8 | data[3])
        z    = (2.0 / 0x8000) * u2s(data[4] << 8 | data[5])
        return (x,y,z)

    def writeByte(self, addr, data):
        d = bytearray([data])
        self.i2c.writeto_mem(self.slvAddr, addr, d)

    def readByte(self, addr, num):
        s = self.i2c.readfrom_mem(self.slvAddr, addr, num)
        return s


# UARTポートを利用する
uart1 = UART(1, 115200, tx=Pin(4), rx=Pin(5))

while True:
    x,y,z = mpu6050(sda=Pin(0), scl=Pin(1)).readXYZ()
    print('x:',x,'y:',y,'z:',z,'uint:mg')
    
    sleep(1)
    
    uart1.write('x:' + str(x)+'y:'+str(y)+'z:'+str(z)+'uint:mg')
    
    sleep(1)

# https://tiblab.net/blog/2021/08/raspberrypi-zero-pico-serial/
# 参考情報
# もう一方はcuコマンドで受け取る
# https://qiita.com/sttn/items/567c9f49b88ff275b51a