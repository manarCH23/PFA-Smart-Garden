import requests
from PyQt6.QtCore import QTimer,QDate,QTime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QLinearGradient
from PyQt6.QtGui import QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 318)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # Set style sheet
        MainWindow.setStyleSheet("""QMainWindow {
        background-color: #3E4491;
    }
""")

        #Alternatively, you can set the style sheet for the central widget
        self.centralwidget.setStyleSheet("""QWidget {
         background-color: #F7A400;
     }
 """)
        
        #########TextEdit#############################

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        self.textEdit.setStyleSheet("""
    QTextEdit {
        font-family: Arial;
        font-size: 14px;
        color: #333333;
        background-color: #F8F8F8;
        border: 1px solid #BDBDBD;
        border-radius: 5px;
        padding: 5px;
    }

    QTextEdit:focus {
        border: 1px solid #4D90FE;
    }
""")
       ########TextEdit2###########################

        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.gridLayout.addWidget(self.textEdit_2, 2, 1, 1, 1)
        self.textEdit_2.setStyleSheet("""
    QTextEdit {
        font-family: Arial;
        font-size: 14px;
        color: #333333;
        background-color: #F8F8F8;
        border: 1px solid #BDBDBD;
        border-radius: 5px;
        padding: 5px;
    }

    QTextEdit:focus {
        border: 1px solid #4D90FE;
    }
""")
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.textEdit_2.setFont(font)
        ##############  logout button  ####################
        self.logout = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.gridLayout.addWidget(self.logout, 0, 2, 1, 1)
        gradient = QLinearGradient(0, 0, 0, self.logout.height())
        gradient.setColorAt(0.0, QColor("#1B75BC"))
        gradient.setColorAt(1.0, QColor("#2E8DCB"))
        self.logout.setStyleSheet(
    "background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                text-align: center;\
                                text-decoration: none;\
                                font-size: 16px;\
                                margin: 4px 2px;"
)

        ########## push button for turn on and turn off  ########################

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton.setStyleSheet("background-color: #3A9Efd; /* Green */ \
                                border: none;\
                                color: white;\
                                padding: 5px 10px;\
                                text-align: center;\
                                text-decoration: none;\
                                font-size: 16px;\
                                margin: 4px 2px;")
        
        ######################################################

        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setStyleSheet("""QWidget {
         background-color: #FFFFFF;
     }
 """)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.dateEdit.setFont(font)
        ###########################################################
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.timeEdit.setTime(QTime.currentTime())
        self.timeEdit.setStyleSheet("""QWidget {
         background-color: #FFFFFF;
     }
 """)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.timeEdit.setFont(font)
        ########################################################

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.menubar.setFont(font)

        #######################################################


        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ####################################################
        self.data_timer = QTimer()
        self.data_timer.timeout.connect(self.Dht11_Data)
        self.data_timer.start(5000)  # 1 minute interval
        
        # Retrieve the initial data
        self.Dht11_Data()
        
    def Dht11_Data(self) :
        try :
            r=requests.get('http://127.0.0.1:8000/api/Dht11/')
            if r.status_code == 200 :
                json = r.json()
                s = json[-1]['data']
                Dht11 = s
                self.textEdit_2.setText(Dht11)
        except :
                self.textEdit_2.setText("Error retrieving data")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logout.setText(_translate("MainWindow", "LOG OUT"))
        self.pushButton.setText(_translate("MainWindow", "TURN ON"))
    