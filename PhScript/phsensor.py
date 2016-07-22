import androidhelper
import socket
import time
import datetime

droid = androidhelper.Android()


port=13373
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.43.236",port)) #connecting to pi as client
droid.makeToast("Starting location fetch") #notify me
while True:
	try:
		droid.startSensingTimed (1,250)
	except:
		print "StartSensing Exception. Sleeping 5 seconds"
		droid.stopSensing ()
		time.sleep(5)
		continue
	curtime = datetime.datetime.now().isoformat()
	location = droid.getLastKnownLocation().result
	location = location.get('network', location.get('gps'))	#fetch location
	accelerometer = droid.sensorsReadAccelerometer().result
	magnetometer = droid.sensorsReadMagnetometer().result
	orientation = droid.sensorsReadOrientation().result	
	data = str(curtime) + "\n" + str(accelerometer) + "\n" + str(magnetometer) + "\n" + str(orientation) + "\n" + str(location)
	print(data) #logging
	s.send(data) #send to server
	time.sleep(1) #wait for 5 seconds
