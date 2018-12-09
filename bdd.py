from bluedot import BlueDot
from signal import pause
import serial

arduino = serial.Serial('/dev/ttyACM0',baudrate=9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1,xonxoff=0,rtscts=0)
sleep(3)

arduino.setDTR(False)
sleep(2)

arduino.flushInput()
arduino.setDTR(True)

bd = BlueDot()

def move(pos):
    if pos.top:
        print("forward")
        arduino.write('f'.encode('utf-8'))
    elif pos.bottom:
        print("backward")
        arduino.write('b'.encode('utf-8'))
    elif pos.left:
        print("left")
        arduino.write('l'.encode('utf-8'))
    elif pos.right:
        print("right")
        arduino.write('r'.encode('utf-8'))

def stop():
    print("stop")
    arduino.write('s'.encode('utf-8'))



bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()