import serial
import time


# Connection to usb port on mac
SerialObject = serial.Serial('/dev/tty.usbmodem7877B8B700181', 9600)

# Default parameters to be changed if required

gcode = open('1002.nc', 'r')
# Confirmed connection with usb
print(SerialObject)

# Code referenced from grbl db
SerialObject.write(str.encode('\r\n\r\n'))
time.sleep(2)
SerialObject.flushInput()
for line in gcode:
    l = line.strip()
    print('sending: ' + l),
    SerialObject.write(str.encode(l + '\n'))
    grbl_out = SerialObject.readline()
    print(' : ' + grbl_out.strip().decode())

# Closing Serial port
gcode.close()
SerialObject.close()
