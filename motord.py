from bluedot import BlueDot
from signal import pause
import serial 

ser=serial.Serial('/dev/ttyACM0',baudrate=9600)

bd = BlueDot()

def move(pos):
    if pos.top:
        ser.write(b'f')
    elif pos.bottom:
        ser.write(b'b')
    elif pos.left:
        ser.write(b'l')
    elif pos.right:
        ser.write(b'r')

def stop():
    print("stop")
    ser.write(b's')

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()