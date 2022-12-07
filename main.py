import serial
# Connection to usb port on mac
SerialObject = serial.Serial('/dev/tty.usbmodem7877B8B700181')

# Default parameters to be changed if required
SerialObject.baudrate = 9600
SerialObject.bytesize = 8
SerialObject.parity = serial.PARITY_EVEN
SerialObject.STOPBITS = serial.STOPBITS_TWO

# Confirmed connection with usb
print(SerialObject)

# Closing Serial port
SerialObject.close()
