#https://api.thingspeak.com/update?api_key=DR1EW65N4Y56029O&field1=31.1
import urllib.request
import serial
import time
from io import StringIO  # Python3
 
 
import sys
old_stdout = sys.stdout
#f = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=DR1EW65N4Y56029O&field1=31.1')
with serial.Serial('COM14', 9600, timeout=1) as ser:
	while 1:
		#time.sleep(5)
		#x = ser.read()          # read one byte
		#print(x)
		#s = ser.read(10)        # read up to ten bytes (timeout)
		#print(s)
		URL=""
		line = ser.readline()   # read a '\n' terminated line
		#print(line)
		temp_URL=StringIO()
		sys.stdout = temp_URL
		print ("https://api.thingspeak.com/update?api_key=DR1EW65N4Y56029O&field1=%s" % (line.decode('UTF-8')))
		sys.stdout = old_stdout
		URL=temp_URL.getvalue()
		f=urllib.request.urlopen(URL)
		print(URL)