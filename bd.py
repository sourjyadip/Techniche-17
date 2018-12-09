from bluedot import BlueDot
from signal import pause

bd = BlueDot()

def move(pos):
    if pos.top:
        print("forward")
    elif pos.bottom:
        print("backward")
    elif pos.left:
        print("left")
    elif pos.right:
        print("right")

def stop():
    print("stop")

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()
