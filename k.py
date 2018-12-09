import cv2
import numpy as np
import serial
from time import sleep
from subprocess import check_output, STDOUT


def capture_frame(fname="image.jpg"):
    """ Returns: result of cv2.imread(fname) """
    while True:
        ret = check_output(['sudo', 'fswebcam', '--no-timestamp',
                            '--no-banner', fname], universal_newlines=True, stderr=STDOUT)
        if "Writing" in ret:
            return cv2.imread(fname)
        else:
            sleep(1)


def ccomp(im):
    # Pass thresholded image to this function

    # MAKE SURE THAT THE BACKGROUND IS BLACK
    # AND THE SHAPE IS WHITE
    # USE INVERTED THRESHOLD

    ccomp = cv2.connectedComponents(im, connectivity=8)
    comp_list = {}
    for (x, y) in np.ndenumerate(ccomp[1]):
        if y != 0:
            comp_list[y] = comp_list.get(y, 0) + 1

    largest_component = max(comp_list, key=comp_list.get)
    indices = np.where(ccomp[1] == largest_component)
    xmin, xmax = min(indices[0]), max(indices[0])
    ymin, ymax = min(indices[1]), max(indices[1])
    return (xmax - xmin, ymax - ymin)


def main():
    arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1, xonxoff=0, rtscts=0)
    sleep(3)
    # Toggle DTR to reset Arduino
    arduino.setDTR(False)
    sleep(2)
    # toss any data already received, see
    # http://pyserial.sourceforge.net/pyserial_api.html#serial.Serial.flushInput
    arduino.flushInput()
    arduino.setDTR(True)

    flag = 0
    print("start writing")
    while flag == 0:
        k = input()
        if k == 's':
            frame = capture_frame()
            given = shape(frame)
            print(given)
            sleep(2)
        elif k == 'd':
            while True:
                arduino.write('t'.encode('utf-8'))
                d = arduino.read()
                print(d)
                if d == b'k':
                    frame1 = capture_frame()
                    now = shape(frame1)
                    print(now)
                    if given == now:
                        arduino.write('f'.encode('utf-8'))
                        flag = 1
                        break


def shape(frame):

    img = frame
    crop_img = img[0:480, 80:560]

    res = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    _, contours, h = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        print(len(approx))

        if len(approx) == 3:
            return "triangle"
        elif len(approx) > 11:
            return "circle"
        else:
            x, y = ccomp(thresh)
            print("could be square or rect: x, y span is ", x, y)
            # TODO: ADJUST HERE
            if abs(x - y) <= 20:
                return "square"
            else:
                return "rectangle"


if __name__ == "__main__":
    main()
