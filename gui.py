# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jul 20 16:47:44 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PH_SENS(object):
    def setupUi(self, PH_SENS):
        PH_SENS.setObjectName(_fromUtf8("PH_SENS"))
        PH_SENS.resize(800, 420)
        self.centralWidget = QtGui.QWidget(PH_SENS)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 721, 341))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(48, 48))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupOBD = QtGui.QGroupBox(self.tab_2)
        self.groupOBD.setGeometry(QtCore.QRect(0, 0, 711, 271))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.groupOBD.setFont(font)
        self.groupOBD.setTitle(_fromUtf8(""))
        self.groupOBD.setObjectName(_fromUtf8("groupOBD"))
        self.lbl3 = QtGui.QLabel(self.groupOBD)
        self.lbl3.setGeometry(QtCore.QRect(0, 180, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3.setFont(font)
        self.lbl3.setAutoFillBackground(True)
        self.lbl3.setFrameShape(QtGui.QFrame.Box)
        self.lbl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl3.setObjectName(_fromUtf8("lbl3"))
        self.lbl1 = QtGui.QLabel(self.groupOBD)
        self.lbl1.setGeometry(QtCore.QRect(0, 0, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl1.setFont(font)
        self.lbl1.setAutoFillBackground(True)
        self.lbl1.setFrameShape(QtGui.QFrame.Box)
        self.lbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1.setObjectName(_fromUtf8("lbl1"))
        self.lbl2 = QtGui.QLabel(self.groupOBD)
        self.lbl2.setGeometry(QtCore.QRect(0, 90, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl2.setFont(font)
        self.lbl2.setAutoFillBackground(True)
        self.lbl2.setFrameShape(QtGui.QFrame.Box)
        self.lbl2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl2.setObjectName(_fromUtf8("lbl2"))
        self.lbl4 = QtGui.QLabel(self.groupOBD)
        self.lbl4.setGeometry(QtCore.QRect(190, 0, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl4.setFont(font)
        self.lbl4.setAutoFillBackground(True)
        self.lbl4.setFrameShape(QtGui.QFrame.Box)
        self.lbl4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl4.setObjectName(_fromUtf8("lbl4"))
        self.lbl5 = QtGui.QLabel(self.groupOBD)
        self.lbl5.setGeometry(QtCore.QRect(190, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl5.setFont(font)
        self.lbl5.setAutoFillBackground(True)
        self.lbl5.setFrameShape(QtGui.QFrame.Box)
        self.lbl5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl5.setObjectName(_fromUtf8("lbl5"))
        self.lbl6 = QtGui.QLabel(self.groupOBD)
        self.lbl6.setGeometry(QtCore.QRect(190, 180, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl6.setFont(font)
        self.lbl6.setAutoFillBackground(True)
        self.lbl6.setFrameShape(QtGui.QFrame.Box)
        self.lbl6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl6.setObjectName(_fromUtf8("lbl6"))
        self.lbl7 = QtGui.QLabel(self.groupOBD)
        self.lbl7.setGeometry(QtCore.QRect(350, 0, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl7.setFont(font)
        self.lbl7.setAutoFillBackground(True)
        self.lbl7.setFrameShape(QtGui.QFrame.Box)
        self.lbl7.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl7.setObjectName(_fromUtf8("lbl7"))
        self.lbl8 = QtGui.QLabel(self.groupOBD)
        self.lbl8.setGeometry(QtCore.QRect(350, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl8.setFont(font)
        self.lbl8.setAutoFillBackground(True)
        self.lbl8.setFrameShape(QtGui.QFrame.Box)
        self.lbl8.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl8.setObjectName(_fromUtf8("lbl8"))
        self.lbl9 = QtGui.QLabel(self.groupOBD)
        self.lbl9.setGeometry(QtCore.QRect(350, 180, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl9.setFont(font)
        self.lbl9.setAutoFillBackground(True)
        self.lbl9.setFrameShape(QtGui.QFrame.Box)
        self.lbl9.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl9.setObjectName(_fromUtf8("lbl9"))
        self.lbl10 = QtGui.QLabel(self.groupOBD)
        self.lbl10.setGeometry(QtCore.QRect(530, 0, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl10.setFont(font)
        self.lbl10.setAutoFillBackground(True)
        self.lbl10.setFrameShape(QtGui.QFrame.Box)
        self.lbl10.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl10.setObjectName(_fromUtf8("lbl10"))
        self.lbl11 = QtGui.QLabel(self.groupOBD)
        self.lbl11.setGeometry(QtCore.QRect(530, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl11.setFont(font)
        self.lbl11.setAutoFillBackground(True)
        self.lbl11.setFrameShape(QtGui.QFrame.Box)
        self.lbl11.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl11.setObjectName(_fromUtf8("lbl11"))
        self.lbl12 = QtGui.QLabel(self.groupOBD)
        self.lbl12.setGeometry(QtCore.QRect(530, 180, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl12.setFont(font)
        self.lbl12.setAutoFillBackground(True)
        self.lbl12.setFrameShape(QtGui.QFrame.Box)
        self.lbl12.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl12.setObjectName(_fromUtf8("lbl12"))
        self.lbl1_res = QtGui.QLabel(self.groupOBD)
        self.lbl1_res.setGeometry(QtCore.QRect(40, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl1_res.setFont(font)
        self.lbl1_res.setAutoFillBackground(True)
        self.lbl1_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl1_res.setText(_fromUtf8(""))
        self.lbl1_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl1_res.setObjectName(_fromUtf8("lbl1_res"))
        self.lbl2_res = QtGui.QLabel(self.groupOBD)
        self.lbl2_res.setGeometry(QtCore.QRect(40, 110, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl2_res.setFont(font)
        self.lbl2_res.setAutoFillBackground(True)
        self.lbl2_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl2_res.setText(_fromUtf8(""))
        self.lbl2_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl2_res.setObjectName(_fromUtf8("lbl2_res"))
        self.lbl3_res = QtGui.QLabel(self.groupOBD)
        self.lbl3_res.setGeometry(QtCore.QRect(40, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3_res.setFont(font)
        self.lbl3_res.setAutoFillBackground(True)
        self.lbl3_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl3_res.setText(_fromUtf8(""))
        self.lbl3_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl3_res.setObjectName(_fromUtf8("lbl3_res"))
        self.lbl4_res = QtGui.QLabel(self.groupOBD)
        self.lbl4_res.setGeometry(QtCore.QRect(210, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl4_res.setFont(font)
        self.lbl4_res.setAutoFillBackground(True)
        self.lbl4_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl4_res.setText(_fromUtf8(""))
        self.lbl4_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl4_res.setObjectName(_fromUtf8("lbl4_res"))
        self.lbl5_res = QtGui.QLabel(self.groupOBD)
        self.lbl5_res.setGeometry(QtCore.QRect(210, 110, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl5_res.setFont(font)
        self.lbl5_res.setAutoFillBackground(True)
        self.lbl5_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl5_res.setText(_fromUtf8(""))
        self.lbl5_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl5_res.setObjectName(_fromUtf8("lbl5_res"))
        self.lbl6_res = QtGui.QLabel(self.groupOBD)
        self.lbl6_res.setGeometry(QtCore.QRect(210, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl6_res.setFont(font)
        self.lbl6_res.setAutoFillBackground(True)
        self.lbl6_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl6_res.setText(_fromUtf8(""))
        self.lbl6_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl6_res.setObjectName(_fromUtf8("lbl6_res"))
        self.lbl9_res = QtGui.QLabel(self.groupOBD)
        self.lbl9_res.setGeometry(QtCore.QRect(380, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl9_res.setFont(font)
        self.lbl9_res.setAutoFillBackground(True)
        self.lbl9_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl9_res.setText(_fromUtf8(""))
        self.lbl9_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl9_res.setObjectName(_fromUtf8("lbl9_res"))
        self.lbl7_res = QtGui.QLabel(self.groupOBD)
        self.lbl7_res.setGeometry(QtCore.QRect(380, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl7_res.setFont(font)
        self.lbl7_res.setAutoFillBackground(True)
        self.lbl7_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl7_res.setText(_fromUtf8(""))
        self.lbl7_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl7_res.setObjectName(_fromUtf8("lbl7_res"))
        self.lbl8_res = QtGui.QLabel(self.groupOBD)
        self.lbl8_res.setGeometry(QtCore.QRect(380, 110, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl8_res.setFont(font)
        self.lbl8_res.setAutoFillBackground(True)
        self.lbl8_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl8_res.setText(_fromUtf8(""))
        self.lbl8_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl8_res.setObjectName(_fromUtf8("lbl8_res"))
        self.lbl12_res = QtGui.QLabel(self.groupOBD)
        self.lbl12_res.setGeometry(QtCore.QRect(560, 200, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl12_res.setFont(font)
        self.lbl12_res.setAutoFillBackground(True)
        self.lbl12_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl12_res.setText(_fromUtf8(""))
        self.lbl12_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl12_res.setObjectName(_fromUtf8("lbl12_res"))
        self.lbl11_res = QtGui.QLabel(self.groupOBD)
        self.lbl11_res.setGeometry(QtCore.QRect(560, 110, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl11_res.setFont(font)
        self.lbl11_res.setAutoFillBackground(True)
        self.lbl11_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl11_res.setText(_fromUtf8(""))
        self.lbl11_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl11_res.setObjectName(_fromUtf8("lbl11_res"))
        self.lbl10_res = QtGui.QLabel(self.groupOBD)
        self.lbl10_res.setGeometry(QtCore.QRect(560, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl10_res.setFont(font)
        self.lbl10_res.setAutoFillBackground(True)
        self.lbl10_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl10_res.setText(_fromUtf8(""))
        self.lbl10_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl10_res.setObjectName(_fromUtf8("lbl10_res"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("OBD.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupPhone = QtGui.QGroupBox(self.tab)
        self.groupPhone.setGeometry(QtCore.QRect(10, -10, 691, 271))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupPhone.setFont(font)
        self.groupPhone.setTitle(_fromUtf8(""))
        self.groupPhone.setObjectName(_fromUtf8("groupPhone"))
        self.lbl_ip = QtGui.QLabel(self.groupPhone)
        self.lbl_ip.setGeometry(QtCore.QRect(10, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_ip.setFont(font)
        self.lbl_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ip.setObjectName(_fromUtf8("lbl_ip"))
        self.lbl_port = QtGui.QLabel(self.groupPhone)
        self.lbl_port.setGeometry(QtCore.QRect(220, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_port.setFont(font)
        self.lbl_port.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_port.setObjectName(_fromUtf8("lbl_port"))
        self.lblacc = QtGui.QLabel(self.groupPhone)
        self.lblacc.setGeometry(QtCore.QRect(0, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblacc.setFont(font)
        self.lblacc.setFrameShape(QtGui.QFrame.Box)
        self.lblacc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblacc.setObjectName(_fromUtf8("lblacc"))
        self.lblmag = QtGui.QLabel(self.groupPhone)
        self.lblmag.setGeometry(QtCore.QRect(0, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblmag.setFont(font)
        self.lblmag.setFrameShape(QtGui.QFrame.Box)
        self.lblmag.setAlignment(QtCore.Qt.AlignCenter)
        self.lblmag.setObjectName(_fromUtf8("lblmag"))
        self.lblori = QtGui.QLabel(self.groupPhone)
        self.lblori.setGeometry(QtCore.QRect(0, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblori.setFont(font)
        self.lblori.setFrameShape(QtGui.QFrame.Box)
        self.lblori.setAlignment(QtCore.Qt.AlignCenter)
        self.lblori.setObjectName(_fromUtf8("lblori"))
        self.lblcompass = QtGui.QLabel(self.groupPhone)
        self.lblcompass.setGeometry(QtCore.QRect(540, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblcompass.setFont(font)
        self.lblcompass.setAlignment(QtCore.Qt.AlignCenter)
        self.lblcompass.setObjectName(_fromUtf8("lblcompass"))
        self.lblltd = QtGui.QLabel(self.groupPhone)
        self.lblltd.setGeometry(QtCore.QRect(0, 200, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblltd.setFont(font)
        self.lblltd.setFrameShape(QtGui.QFrame.Box)
        self.lblltd.setAlignment(QtCore.Qt.AlignCenter)
        self.lblltd.setObjectName(_fromUtf8("lblltd"))
        self.lbllgd = QtGui.QLabel(self.groupPhone)
        self.lbllgd.setGeometry(QtCore.QRect(0, 240, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbllgd.setFont(font)
        self.lbllgd.setFrameShape(QtGui.QFrame.Box)
        self.lbllgd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbllgd.setObjectName(_fromUtf8("lbllgd"))
        self.lblacc_x = QtGui.QLabel(self.groupPhone)
        self.lblacc_x.setGeometry(QtCore.QRect(150, 50, 111, 41))
        self.lblacc_x.setFrameShape(QtGui.QFrame.Box)
        self.lblacc_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lblacc_x.setObjectName(_fromUtf8("lblacc_x"))
        self.lblacc_y = QtGui.QLabel(self.groupPhone)
        self.lblacc_y.setGeometry(QtCore.QRect(260, 50, 111, 41))
        self.lblacc_y.setFrameShape(QtGui.QFrame.Box)
        self.lblacc_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lblacc_y.setObjectName(_fromUtf8("lblacc_y"))
        self.lblacc_z = QtGui.QLabel(self.groupPhone)
        self.lblacc_z.setGeometry(QtCore.QRect(370, 50, 111, 41))
        self.lblacc_z.setFrameShape(QtGui.QFrame.Box)
        self.lblacc_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lblacc_z.setObjectName(_fromUtf8("lblacc_z"))
        self.lblacc_x_2 = QtGui.QLabel(self.groupPhone)
        self.lblacc_x_2.setGeometry(QtCore.QRect(540, 110, 111, 51))
        self.lblacc_x_2.setFrameShape(QtGui.QFrame.Box)
        self.lblacc_x_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblacc_x_2.setObjectName(_fromUtf8("lblacc_x_2"))
        self.lblmag_z = QtGui.QLabel(self.groupPhone)
        self.lblmag_z.setGeometry(QtCore.QRect(370, 100, 111, 41))
        self.lblmag_z.setFrameShape(QtGui.QFrame.Box)
        self.lblmag_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lblmag_z.setObjectName(_fromUtf8("lblmag_z"))
        self.lblmag_y = QtGui.QLabel(self.groupPhone)
        self.lblmag_y.setGeometry(QtCore.QRect(260, 100, 111, 41))
        self.lblmag_y.setFrameShape(QtGui.QFrame.Box)
        self.lblmag_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lblmag_y.setObjectName(_fromUtf8("lblmag_y"))
        self.lblmag_x = QtGui.QLabel(self.groupPhone)
        self.lblmag_x.setGeometry(QtCore.QRect(150, 100, 111, 41))
        self.lblmag_x.setFrameShape(QtGui.QFrame.Box)
        self.lblmag_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lblmag_x.setObjectName(_fromUtf8("lblmag_x"))
        self.lblori_z = QtGui.QLabel(self.groupPhone)
        self.lblori_z.setGeometry(QtCore.QRect(370, 150, 111, 41))
        self.lblori_z.setFrameShape(QtGui.QFrame.Box)
        self.lblori_z.setAlignment(QtCore.Qt.AlignCenter)
        self.lblori_z.setObjectName(_fromUtf8("lblori_z"))
        self.lblori_x = QtGui.QLabel(self.groupPhone)
        self.lblori_x.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.lblori_x.setFrameShape(QtGui.QFrame.Box)
        self.lblori_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lblori_x.setObjectName(_fromUtf8("lblori_x"))
        self.lblori_y = QtGui.QLabel(self.groupPhone)
        self.lblori_y.setGeometry(QtCore.QRect(260, 150, 111, 41))
        self.lblori_y.setFrameShape(QtGui.QFrame.Box)
        self.lblori_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lblori_y.setObjectName(_fromUtf8("lblori_y"))
        self.lbllati = QtGui.QLabel(self.groupPhone)
        self.lbllati.setGeometry(QtCore.QRect(150, 200, 331, 31))
        self.lbllati.setFrameShape(QtGui.QFrame.Box)
        self.lbllati.setAlignment(QtCore.Qt.AlignCenter)
        self.lbllati.setObjectName(_fromUtf8("lbllati"))
        self.lbllongi = QtGui.QLabel(self.groupPhone)
        self.lbllongi.setGeometry(QtCore.QRect(150, 240, 331, 31))
        self.lbllongi.setFrameShape(QtGui.QFrame.Box)
        self.lbllongi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbllongi.setObjectName(_fromUtf8("lbllongi"))
        self.lbl_ip_res = QtGui.QLabel(self.groupPhone)
        self.lbl_ip_res.setGeometry(QtCore.QRect(50, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_ip_res.setFont(font)
        self.lbl_ip_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ip_res.setObjectName(_fromUtf8("lbl_ip_res"))
        self.lbl_port_res = QtGui.QLabel(self.groupPhone)
        self.lbl_port_res.setGeometry(QtCore.QRect(280, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_port_res.setFont(font)
        self.lbl_port_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_port_res.setObjectName(_fromUtf8("lbl_port_res"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("android-phone-color.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lbl_sug_gear = QtGui.QLabel(self.tab_3)
        self.lbl_sug_gear.setGeometry(QtCore.QRect(10, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sug_gear.setFont(font)
        self.lbl_sug_gear.setAutoFillBackground(False)
        self.lbl_sug_gear.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sug_gear.setObjectName(_fromUtf8("lbl_sug_gear"))
        self.lbl_veh_speed = QtGui.QLabel(self.tab_3)
        self.lbl_veh_speed.setGeometry(QtCore.QRect(260, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_veh_speed.setFont(font)
        self.lbl_veh_speed.setAutoFillBackground(False)
        self.lbl_veh_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_veh_speed.setObjectName(_fromUtf8("lbl_veh_speed"))
        self.lbl_eco_mode = QtGui.QLabel(self.tab_3)
        self.lbl_eco_mode.setGeometry(QtCore.QRect(520, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eco_mode.setFont(font)
        self.lbl_eco_mode.setAutoFillBackground(False)
        self.lbl_eco_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eco_mode.setObjectName(_fromUtf8("lbl_eco_mode"))
        self.lbl_sug_gear_res = QtGui.QLabel(self.tab_3)
        self.lbl_sug_gear_res.setGeometry(QtCore.QRect(10, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sug_gear_res.setFont(font)
        self.lbl_sug_gear_res.setAutoFillBackground(False)
        self.lbl_sug_gear_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_sug_gear_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_sug_gear_res.setObjectName(_fromUtf8("lbl_sug_gear_res"))
        self.lbl_veh_speed_res = QtGui.QLabel(self.tab_3)
        self.lbl_veh_speed_res.setGeometry(QtCore.QRect(250, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_veh_speed_res.setFont(font)
        self.lbl_veh_speed_res.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_veh_speed_res.setAutoFillBackground(False)
        self.lbl_veh_speed_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_veh_speed_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_veh_speed_res.setObjectName(_fromUtf8("lbl_veh_speed_res"))
        self.lbl_eco_mode_res = QtGui.QLabel(self.tab_3)
        self.lbl_eco_mode_res.setGeometry(QtCore.QRect(490, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eco_mode_res.setFont(font)
        self.lbl_eco_mode_res.setAutoFillBackground(False)
        self.lbl_eco_mode_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_eco_mode_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eco_mode_res.setObjectName(_fromUtf8("lbl_eco_mode_res"))
        self.lbl_avg_veh_speed_res = QtGui.QLabel(self.tab_3)
        self.lbl_avg_veh_speed_res.setGeometry(QtCore.QRect(250, 160, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_avg_veh_speed_res.setFont(font)
        self.lbl_avg_veh_speed_res.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_avg_veh_speed_res.setAutoFillBackground(False)
        self.lbl_avg_veh_speed_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_avg_veh_speed_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_avg_veh_speed_res.setObjectName(_fromUtf8("lbl_avg_veh_speed_res"))
        self.lbl_avg_veh_speed = QtGui.QLabel(self.tab_3)
        self.lbl_avg_veh_speed.setGeometry(QtCore.QRect(260, 140, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_avg_veh_speed.setFont(font)
        self.lbl_avg_veh_speed.setAutoFillBackground(False)
        self.lbl_avg_veh_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_avg_veh_speed.setObjectName(_fromUtf8("lbl_avg_veh_speed"))
        self.lbl_eng_rpm = QtGui.QLabel(self.tab_3)
        self.lbl_eng_rpm.setGeometry(QtCore.QRect(10, 140, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eng_rpm.setFont(font)
        self.lbl_eng_rpm.setAutoFillBackground(False)
        self.lbl_eng_rpm.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eng_rpm.setObjectName(_fromUtf8("lbl_eng_rpm"))
        self.lbl_eng_rpm_res = QtGui.QLabel(self.tab_3)
        self.lbl_eng_rpm_res.setGeometry(QtCore.QRect(10, 160, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eng_rpm_res.setFont(font)
        self.lbl_eng_rpm_res.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_eng_rpm_res.setAutoFillBackground(False)
        self.lbl_eng_rpm_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_eng_rpm_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eng_rpm_res.setObjectName(_fromUtf8("lbl_eng_rpm_res"))
        self.lbl_eng_load = QtGui.QLabel(self.tab_3)
        self.lbl_eng_load.setGeometry(QtCore.QRect(500, 140, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eng_load.setFont(font)
        self.lbl_eng_load.setAutoFillBackground(False)
        self.lbl_eng_load.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eng_load.setObjectName(_fromUtf8("lbl_eng_load"))
        self.lbl_eng_load_res = QtGui.QLabel(self.tab_3)
        self.lbl_eng_load_res.setGeometry(QtCore.QRect(490, 160, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eng_load_res.setFont(font)
        self.lbl_eng_load_res.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_eng_load_res.setAutoFillBackground(False)
        self.lbl_eng_load_res.setFrameShape(QtGui.QFrame.Box)
        self.lbl_eng_load_res.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_eng_load_res.setObjectName(_fromUtf8("lbl_eng_load_res"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Analysis.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon2, _fromUtf8(""))
        self.lblTime = QtGui.QLabel(self.centralWidget)
        self.lblTime.setGeometry(QtCore.QRect(740, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setAutoFillBackground(True)
        self.lblTime.setFrameShape(QtGui.QFrame.Box)
        self.lblTime.setText(_fromUtf8(""))
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName(_fromUtf8("lblTime"))
        self.lblCounter = QtGui.QLabel(self.centralWidget)
        self.lblCounter.setGeometry(QtCore.QRect(740, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCounter.setFont(font)
        self.lblCounter.setAutoFillBackground(True)
        self.lblCounter.setFrameShape(QtGui.QFrame.Box)
        self.lblCounter.setText(_fromUtf8(""))
        self.lblCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCounter.setObjectName(_fromUtf8("lblCounter"))
        PH_SENS.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(PH_SENS)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        PH_SENS.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(PH_SENS)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        PH_SENS.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(PH_SENS)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        PH_SENS.setStatusBar(self.statusBar)
        self.actionExit = QtGui.QAction(PH_SENS)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PH_SENS)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PH_SENS)

    def retranslateUi(self, PH_SENS):
        PH_SENS.setWindowTitle(_translate("PH_SENS", "OBD_PHONE_SENSOR", None))
        self.lbl3.setText(_translate("PH_SENS", "unused", None))
        self.lbl1.setText(_translate("PH_SENS", "unused", None))
        self.lbl2.setText(_translate("PH_SENS", "unused", None))
        self.lbl4.setText(_translate("PH_SENS", "unused", None))
        self.lbl5.setText(_translate("PH_SENS", "unused", None))
        self.lbl6.setText(_translate("PH_SENS", "unused", None))
        self.lbl7.setText(_translate("PH_SENS", "unused", None))
        self.lbl8.setText(_translate("PH_SENS", "unused", None))
        self.lbl9.setText(_translate("PH_SENS", "unused", None))
        self.lbl10.setText(_translate("PH_SENS", "unused", None))
        self.lbl11.setText(_translate("PH_SENS", "unused", None))
        self.lbl12.setText(_translate("PH_SENS", "unused", None))
        self.lbl_ip.setText(_translate("PH_SENS", "IP", None))
        self.lbl_port.setText(_translate("PH_SENS", "Port", None))
        self.lblacc.setText(_translate("PH_SENS", "Accelerometer", None))
        self.lblmag.setText(_translate("PH_SENS", "Magnetometer", None))
        self.lblori.setText(_translate("PH_SENS", "Orientation", None))
        self.lblcompass.setText(_translate("PH_SENS", "COMPASS", None))
        self.lblltd.setText(_translate("PH_SENS", "Latitude", None))
        self.lbllgd.setText(_translate("PH_SENS", "Longitude", None))
        self.lblacc_x.setText(_translate("PH_SENS", "x", None))
        self.lblacc_y.setText(_translate("PH_SENS", "y", None))
        self.lblacc_z.setText(_translate("PH_SENS", "z", None))
        self.lblacc_x_2.setText(_translate("PH_SENS", "N", None))
        self.lblmag_z.setText(_translate("PH_SENS", "z", None))
        self.lblmag_y.setText(_translate("PH_SENS", "y", None))
        self.lblmag_x.setText(_translate("PH_SENS", "x", None))
        self.lblori_z.setText(_translate("PH_SENS", "z", None))
        self.lblori_x.setText(_translate("PH_SENS", "x", None))
        self.lblori_y.setText(_translate("PH_SENS", "y", None))
        self.lbllati.setText(_translate("PH_SENS", "lati", None))
        self.lbllongi.setText(_translate("PH_SENS", "longi", None))
        self.lbl_ip_res.setText(_translate("PH_SENS", "198.168.2.1", None))
        self.lbl_port_res.setText(_translate("PH_SENS", "13373", None))
        self.lbl_sug_gear.setText(_translate("PH_SENS", "SUGGESTED GEAR", None))
        self.lbl_veh_speed.setText(_translate("PH_SENS", "VEHICLE SPEED", None))
        self.lbl_eco_mode.setText(_translate("PH_SENS", "ECO MODE", None))
        self.lbl_sug_gear_res.setText(_translate("PH_SENS", "N", None))
        self.lbl_veh_speed_res.setText(_translate("PH_SENS", "0", None))
        self.lbl_eco_mode_res.setText(_translate("PH_SENS", "OFF", None))
        self.lbl_avg_veh_speed_res.setText(_translate("PH_SENS", "0", None))
        self.lbl_avg_veh_speed.setText(_translate("PH_SENS", "AVG VEH SPEED", None))
        self.lbl_eng_rpm.setText(_translate("PH_SENS", "ENG RPM", None))
        self.lbl_eng_rpm_res.setText(_translate("PH_SENS", "0", None))
        self.lbl_eng_load.setText(_translate("PH_SENS", "ENG LOAD", None))
        self.lbl_eng_load_res.setText(_translate("PH_SENS", "OK", None))
        self.menuFile.setTitle(_translate("PH_SENS", "&file", None))
        self.actionExit.setText(_translate("PH_SENS", "&exit", None))

