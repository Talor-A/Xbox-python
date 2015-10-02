import serial
import struct
import time

ser = serial.Serial('/dev/ttymxc3',115200,timeout=1)
ser.flushOutput()
print 'Serial connected'

# let it initialize
time.sleep(2)


while True: 
	ser.write(struct.pack('>B', 45))
	time.sleep(1) 		# delay for 1 second
	print ord(ser.readline())

	ser.write(struct.pack('>B', 180))
	time.sleep(1) 		# delay for 1 second
	print ord(ser.readline())
