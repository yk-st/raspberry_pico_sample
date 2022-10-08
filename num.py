from machine import Pin
import time

display_list = [11,10,21,20,19,12,13]
dotPin=22
display_obj=[]

arrSeg = [[1,1,1,1,1,1,0], # -> arrSeq[0] displays 0
          [0,1,1,0,0,0,0], # -> arrSeq[1] displays 1
          [1,1,0,1,1,0,1], # -> arrSeq[2] displays 2
          [1,1,1,1,0,0,1], # -> arrSeq[3] displays 3
          [0,1,1,0,0,1,1], # -> arrSeq[4] displays 4
          [1,0,1,1,0,1,1], # -> arrSeq[5] displays 5
          [1,0,1,1,1,1,1], # -> arrSeq[6] displays 6
          [1,1,1,0,0,0,0], # -> arrSeq[7] displays 7
          [1,1,1,1,1,1,1], # -> arrSeq[8] displays 8
          [1,1,1,1,0,1,1]] # -> arrSeq[9] displays 9]

def display_seg(toDisplay):
    numDisplay = int(toDisplay.replace(".", ""))
    for a in range(7):
        #pinのvalueを1か9にする
        display_obj[a].value(arrSeg[numDisplay][a])

    if toDisplay.count(".") == 1:
        dot_obj.value(1)
    else:
        dot_obj.value(0)


for seg in display_list:
    display_obj.append(Pin(seg, Pin.OUT))

dot_obj=Pin(dotPin, Pin.OUT)


for i in range(0,10):
    print(i)
    display_seg(str(i) + ".")
    time.sleep(1)

