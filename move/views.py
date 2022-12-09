from django.shortcuts import render
import serial
import time
from pathlib import Path
from django.http import HttpResponse

fileLocation = Path("1002.nc")
initial = '1002.nc'

# Creating connection with usb connection
s = serial.Serial("/dev/tty.usbmodem7877B8B700181", 9600)
gcode = open(initial, 'r')


# Create your views here.
def boot(request):
    s.write(str.encode("\r\n\r\n"))
    time.sleep(2)
    s.flushInput()
    print(gcode.read())
    for line in gcode:
        l = line.split()
        s.write(str.encode(l + '\n'))
        grbl_out = s.readline()
        print(" : " + grbl_out.strip().decode())

    return HttpResponse('Initialised')


def move_forward(request):
    xPosition = 0.0
    yPosition = 0.0
    zPosition = 0.0
    step = 0
    s.write(
        str.encode(("G92 X%d Y%d Z%d F2000 \n" %
                    (xPosition, yPosition, zPosition)))
    )

    print(("X%d Y%d Z%d\n" % (xPosition, yPosition, zPosition)))
    while (step < 20):
        s.write(
            str.encode((" X%d Y%d Z%d F2000 \n" %
                        (xPosition, yPosition, zPosition)))
        )
        xPosition = xPosition + 1
        grbl_out = s.readline()
        print(" : " + grbl_out.strip().decode())
        step = step + 1

    s.write(
        str.encode(("G92 X%d Y%d Z%d F2000 \n" %
                    (xPosition, yPosition, zPosition)))
    )

    return HttpResponse('forward 5 steps')


def move_backward(request):
    xPosition = 0.0
    yPosition = 0.0
    zPosition = 0.0
    step = 0
    s.write(
        str.encode(("G92 X%d Y%d Z%d F2000 \n" %
                    (xPosition, yPosition, zPosition)))
    )

    print(("X%d Y%d Z%d\n" % (xPosition, yPosition, zPosition)))
    while (step < 20):
        s.write(
            str.encode((" X%d Y%d Z%d F2000 \n" %
                        (xPosition, yPosition, zPosition)))
        )
        xPosition = xPosition - 1
        grbl_out = s.readline()
        print(" : " + grbl_out.strip().decode())
        step = step + 1

    s.write(
        str.encode(("G92 X%d Y%d Z%d F2000 \n" %
                    (xPosition, yPosition, zPosition)))
    )

    return HttpResponse('forward 5 steps')
