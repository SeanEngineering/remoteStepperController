import serial
import time
from pynput.keyboard import Key, Controller, Listener
import keyboard


# Connection to usb port on mac
SerialObject = serial.Serial("/dev/tty.usbmodem7877B8B700181", 9600)

# Default parameters to be changed if required

gcode = open("1002.nc", "r")
# Confirmed connection with usb
print(SerialObject)

# Code referenced from grbl db
SerialObject.write(str.encode("\r\n\r\n"))

key = "w"


xPosition = 0.0
yPostion = 0.0
zPostion = 0.0
time.sleep(2)
SerialObject.flushInput()
for line in gcode:
    l = line.strip()
    print("sending: " + l),

    SerialObject.write(str.encode(l + "\n"))
    grbl_out = SerialObject.readline()
    print(" : " + grbl_out.strip().decode())

while True:
    keyboard.wait("w")
    print(("X%d Y%d Z%d\n" % (xPosition, yPostion, zPostion)))
    SerialObject.write(
        str.encode(("X%d Y%d Z%d F2000 \n" % (xPosition, yPostion, zPostion)))
    )
    xPosition = xPosition + 0.1
    grbl_out = SerialObject.readline()
    print(" : " + grbl_out.strip().decode())


# Closing Serial port
gcode.close()
SerialObject.close()
