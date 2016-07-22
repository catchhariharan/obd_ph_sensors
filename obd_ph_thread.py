#!/usr/bin/env python
from threading import *
import subprocess
import time
from datetime import datetime
import socket
#import SocketServer
#import json
import sys
from PyQt4 import QtCore, QtGui
import gui
from obd_capture import OBD_Capture
from math import sqrt

OneSecTimer = 0
SecCounter = 0
GearState = 0
VehicleSpeed = 0
EngineRPM = 0
NeutralTimer = 0
EcoModeState = "OFF"
EngineLoadState = "OK"
EcoTimer = 0
VehSpeedTimer = 0
AvgVehSpeed = 0
AvgVehSpeedList = []
mylist = [0,0,0,0,0,0,0,0,0,0]

def updatelcd(myTimer):
	global SecCounter
	global OneSecTimer
	OneSec = 1/ myTimer
	
	if OneSecTimer >= OneSec - myTimer:
		OneSecTimer = 0
		SecCounter = SecCounter + 1
	else:
		OneSecTimer = OneSecTimer + 1


def AverageVehicleSpeed(myTimer):
	global AvgVehSpeed
	global VehSpeedTimer
	OneSecCounter = 1/ myTimer
	
	if VehSpeedTimer >= OneSecCounter - myTimer:
		VehSpeedTimer = 0
		AvgVehSpeedList.insert(0,VehicleSpeed)
		num_items = len(AvgVehSpeedList)
		AvgVehSpeed = round(float(sum(AvgVehSpeedList)/num_items),2)
	else:
		VehSpeedTimer = VehSpeedTimer + 1
	
def EcoMode(myTimer):
	global EcoModeState
	global mylist
	global EcoTimer
	OneSecCounter = 1/ myTimer
	if VehicleSpeed != 17:
		if EcoTimer >= OneSecCounter - myTimer:
			EcoTimer = 0
			shift_left_once(mylist,VehicleSpeed)
			#print mylist
			sd = standard_deviation(mylist,True)

			if sd <= 5 and VehicleSpeed >25 and VehicleSpeed<100:
				EcoModeState = "ON"
			else:
				EcoModeState = "OFF"
		else:
			EcoTimer = EcoTimer + 1

def EngineLoadCalc(myTimer):
	global EngineLoadState

	if CalcEngineLoad >= 95:
		EngineLoadState = "HI"
	else:
		EngineLoadState = "OK"


def updategear(myTimer):
	global GearState
	global NeutralTimer
	global VehicleSpeed
	global EngineRPM
	global CalcEngineLoad
	FourSecCounter = 4/myTimer

	newoutfile = open("obdsensors.log","r+")
	for i in range(1,13):
		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] == "Vehicle Speed":
			VehicleSpeed = round(float(buf[1]),2)
		if buf[0] == "Engine RPM":
			EngineRPM = round(float(buf[1]),2)
		if buf[0] == "Calc Load Value":
			CalcEngineLoad = round(float(buf[1]),2)
		pass
	newoutfile.close()

	if VehicleSpeed >= 1  and (GearState == 0 or GearState == 'N') :
		GearState = 1
		NeutralTimer = 0
	elif VehicleSpeed > 5  and GearState == 1:
		GearState = 2
		NeutralTimer = 0
	elif VehicleSpeed > 25  and GearState == 2:
		GearState = 3
		NeutralTimer = 0
	elif VehicleSpeed > 40  and GearState == 3:
		GearState = 4
		NeutralTimer = 0
	elif VehicleSpeed > 55  and GearState == 4:
		GearState = 5
		NeutralTimer = 0
	elif VehicleSpeed < 50  and GearState == 5:
		GearState = 4
		NeutralTimer = 0
	elif VehicleSpeed < 35  and GearState == 4:
		GearState = 3
		NeutralTimer = 0
	elif VehicleSpeed < 20  and GearState == 3:
		GearState = 2
		NeutralTimer = 0
	elif VehicleSpeed < 10  and GearState == 2:
		GearState = 1
		NeutralTimer = 0
	elif VehicleSpeed == 0:
		NeutralTimer = NeutralTimer + 1
		GearState = 1
		
	if VehicleSpeed == 0 and NeutralTimer >= FourSecCounter:
		GearState = str('N')

 
 
def standard_deviation(lst, population=True):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
 
    if population is True:
#        print('This is POPULATION standard deviation.')
        variance = ssd / num_items
    else:
        print('This is SAMPLE standard deviation.')
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)

#    print('The mean of {} is {}.'.format(lst, mean))
#    print('The differences are {}.'.format(differences))
#    print('The sum of squared differences is {}.'.format(ssd))
#    print('The variance is {}.'.format(variance))
#    print('The standard deviation is {}.'.format(sd))
#    print('--------------------------')

    return sd
 

def shift_left_once(mylist,newnum):
	 temp = newnum
	 for index in range (len(mylist)-1):
		 mylist[index] = mylist[index+1]

	 mylist[index+1] = temp

 
class StartQT4(QtGui.QMainWindow,gui.Ui_PH_SENS):
	def __init__(self,parent=None):
		super(StartQT4,self).__init__(parent)
		self.setupUi(self)
		self. initbg()

		self.actionExit.triggered.connect(self.close)
		t = Thread(target=handleClient1)
		t2 = Thread(target=handleClient2)
		t3 = Thread(target=handleClient3)
		t4 = Thread(target=handleClient4)
		t.start()
		t2.start()
		t3.start()
		t4.start()
#		self.btnUpdate.clicked.connect(self.update_Ui)
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update_Ui)
		self.timer.start(200)
		ipnum = subprocess.check_output(["hostname","-I"])
		port = 13373
		self.lbl_port_res.setText(str(port))
		if ipnum.strip() != "" :
			self.lbl_ip_res.setText(str(ipnum.strip()))
		else:
			self.lbl_ip_res.setText("Not Connected")


	def initbg(self):
		palet = QtGui.QPalette()
		palet.setColor(QtGui.QPalette.Background,QtCore.Qt.black)
		self.setPalette(palet)
		palet.setColor(QtGui.QPalette.Background,QtCore.Qt.black)
		self.tabWidget.setPalette(palet)
		self.tabWidget.setStyleSheet("QWidget {background-color: black}")
		
		
		palet.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
		self.lbl1.setPalette(palet)
		self.lbl2.setPalette(palet)
		self.lbl3.setPalette(palet)
		self.lbl4.setPalette(palet)
		self.lbl5.setPalette(palet)
		self.lbl6.setPalette(palet)
		self.lbl7.setPalette(palet)
		self.lbl8.setPalette(palet)
		self.lbl8.setPalette(palet)
		self.lbl9.setPalette(palet)
		self.lbl10.setPalette(palet)
		self.lbl11.setPalette(palet)
		self.lbl12.setPalette(palet)

		self.lbl_ip.setPalette(palet)
		self.lbl_port.setPalette(palet)

		self.lblacc.setPalette(palet)
		self.lblmag.setPalette(palet)
		self.lblori.setPalette(palet)
		
		self.lbl_sug_gear.setPalette(palet)
		self.lbl_veh_speed.setPalette(palet)
		self.lbl_eng_rpm.setPalette(palet)
		self.lbl_avg_veh_speed.setPalette(palet)		
		self.lbl_eco_mode.setPalette(palet)
		self.lbl_eng_load.setPalette(palet)
		
		palet.setColor(QtGui.QPalette.Foreground,QtCore.Qt.white)
		self.lbl1_res.setPalette(palet)
		self.lbl2_res.setPalette(palet)
		self.lbl3_res.setPalette(palet)
		self.lbl4_res.setPalette(palet)
		self.lbl5_res.setPalette(palet)
		self.lbl6_res.setPalette(palet)
		self.lbl7_res.setPalette(palet)
		self.lbl8_res.setPalette(palet)
		self.lbl9_res.setPalette(palet)
		self.lbl10_res.setPalette(palet)
		self.lbl11_res.setPalette(palet)
		self.lbl12_res.setPalette(palet)
		self.lblTime.setPalette(palet)
		self.lblCounter.setPalette(palet)

		self.lbl_ip_res.setPalette(palet)
		self.lbl_port_res.setPalette(palet)

		self.lblacc_x.setPalette(palet)
		self.lblacc_y.setPalette(palet)
		self.lblacc_z.setPalette(palet)

		self.lblmag_x.setPalette(palet)
		self.lblmag_y.setPalette(palet)
		self.lblmag_z.setPalette(palet)

		self.lblori_x.setPalette(palet)
		self.lblori_y.setPalette(palet)
		self.lblori_z.setPalette(palet)

		self.lbl_sug_gear_res.setPalette(palet)
		self.lbl_veh_speed_res.setPalette(palet)
		self.lbl_eng_rpm_res.setPalette(palet)
		self.lbl_avg_veh_speed_res.setPalette(palet)
		self.lbl_eco_mode_res.setPalette(palet)
		self.lbl_eng_load_res.setPalette(palet)
				
	def update_Ui(self):
		#print "UPDATE"
		self.lbl_eco_mode_res.setText(EcoModeState)
		self.lbl_sug_gear_res.setText(str(GearState))
		self.lbl_veh_speed_res.setText(str(VehicleSpeed))
		self.lbl_avg_veh_speed_res.setText(str(AvgVehSpeed))
		self.lbl_eng_rpm_res.setText(str(EngineRPM))
		self.lbl_eng_load_res.setText(str(EngineLoadState))
		
		newoutfile = open("obdsensors.log","r+")
		buf = newoutfile.readline().strip()
		buf = newoutfile.readline().strip()

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl1.setText(buf[0])
			self.lbl1_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl2.setText(buf[0])
			self.lbl2_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl3.setText(buf[0])
			self.lbl3_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl4.setText(buf[0])
			self.lbl4_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		if buf != "":
			self.lbl5.setText(buf[0])
			self.lbl5_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl6.setText(buf[0])
			self.lbl6_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl7.setText(buf[0])
			self.lbl7_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		if buf != "":
			self.lbl8.setText(buf[0])
			self.lbl8_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		if buf != "":
			self.lbl9.setText(buf[0])
			self.lbl9_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl10.setText(buf[0])
			self.lbl10_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl11.setText(buf[0])
			self.lbl11_res.setText(str(round(float(buf[1]),2)))

		buf = newoutfile.readline().split('=')
		buf[0] = buf[0].strip()
		if buf[0] != "":
			self.lbl12.setText(buf[0])
			self.lbl12_res.setText(str(round(float(buf[1]),2)))

		newoutfile.close()

		localtime = datetime.now()
		current_time = str(localtime.hour)+":"+str(localtime.minute)+":"+str(localtime.second)

		self.lblTime.setText(current_time)
		self.lblCounter.setText(str(SecCounter))

		outfile=open("phsensors.log","r+")
		phcurtime = outfile.readline()
		
		accmeter = outfile.readline().strip().lstrip("[").rstrip("]").splitlines()
		newaccmeter = accmeter[0].split(",")

		magmeter = outfile.readline().strip().lstrip("[").rstrip("]").splitlines()
		newmagmeter = magmeter[0].split(",")

		orimeter = outfile.readline().strip().lstrip("[").rstrip("]").splitlines()
		neworimeter = orimeter[0].split(",")

#		self.btnUpdate.setText("UPDATE")

		self.lblacc_x.setText(str(round(float(newaccmeter[0]),4)))
		self.lblacc_y.setText(str(round(float(newaccmeter[1]),4)))
		self.lblacc_z.setText(str(round(float(newaccmeter[2]),4)))

		self.lblmag_x.setText(str(round(float(newmagmeter[0]),4)))
		self.lblmag_y.setText(str(round(float(newmagmeter[1]),4)))
		self.lblmag_z.setText(str(round(float(newmagmeter[2]),4)))

		self.lblori_x.setText(str(round(float(neworimeter[0]),4)))
		self.lblori_y.setText(str(round(float(neworimeter[1]),4)))
		self.lblori_z.setText(str(round(float(neworimeter[2]),4)))

		outfile.close()

		


def handleClient1():
	while (True):
		try:
			sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			ipnum = subprocess.check_output(["hostname","-I"])
			port = 13373
			sock.bind((ipnum,port))
			sock.listen(2)
			(client,(ip,port))=sock.accept()
			print "Phone Connected"

			while(True):
				#print "Client 1"
				phdata = client.recv(1024).strip()
				#print phdata, 'is my ph data'
				if phdata == "" :
					sock.listen(2)
					(client,(ip,port))=sock.accept()
				outfile=open("phsensors.log","w")
				outfile.write(str(phdata))
				outfile.close()
				time.sleep(1) # wait 5 seconds
			
		except:
			print "HOTSPOT / TETHERING NOT CONNECTED, Trying Again"
		
		time.sleep(3)
		
		
def handleClient2():
	o = OBD_Capture()
	o.connect()
	time.sleep(3)

	while(True):
		if not o.is_connected():
			print "Not connected, Try again"
			o.connect()
			time.sleep(3)
		else:
			#print "Capturing DATA"
			obdsens = o.capture_data()
			#print obdsens
			outfile=open("obdsensors.log","w")
			outfile.write(str(obdsens))
			outfile.close()

		#print "Client 2"
		time.sleep(200/1000) # wait 2 seconds


def handleClient3():
	mylist = [0,0,0,0,0,0,0,0,0,0]
	myTimer = 0.2
	while True:
		#print "client 4"
		updatelcd(myTimer)
		updategear(myTimer)
		EcoMode(myTimer)
		AverageVehicleSpeed(myTimer)
		EngineLoadCalc(myTimer)

		time.sleep(myTimer)

def handleClient4():
	while True:
		#print "Client 3"
		time.sleep(10)
		

if __name__=="__main__":

	app = QtGui.QApplication(sys.argv)
	myapp=StartQT4()
	myapp.show()
	#sys.exit(app.exec_())
	app.exec_()
