# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 350, 771, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 9, 391, 321))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 0, 1, 1, 1)
        self.Year = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Year.setObjectName("Year")
        self.gridLayout.addWidget(self.Year, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Rej = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Rej.setObjectName("Rej")
        self.gridLayout.addWidget(self.Rej, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)
        self.Country = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Country.setObjectName("Country")
        self.gridLayout.addWidget(self.Country, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(20, 80, 161, 25))
        self.save.setObjectName("save")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(200, 80, 181, 25))
        self.load.setObjectName("load")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 200, 191, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(20, 230, 71, 25))
        self.find.setObjectName("find")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 230, 111, 25))
        self.comboBox.setObjectName("comboBox")
        self.word = QtWidgets.QLineEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(20, 130, 331, 25))
        self.word.setObjectName("word")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(260, 160, 89, 25))
        self.change.setObjectName("change")
        self.id = QtWidgets.QComboBox(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(20, 160, 111, 25))
        self.id.setObjectName("id")
        self.pole = QtWidgets.QComboBox(self.centralwidget)
        self.pole.setGeometry(QtCore.QRect(140, 160, 111, 25))
        self.pole.setObjectName("pole")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(20, 270, 89, 25))
        self.delete_2.setObjectName("delete_2")
        self.id_2 = QtWidgets.QComboBox(self.centralwidget)
        self.id_2.setGeometry(QtCore.QRect(120, 270, 111, 25))
        self.id_2.setObjectName("id_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "База фильмов"))
        self.groupBox.setTitle(_translate("MainWindow", "Добавить запись"))
        self.label_4.setText(_translate("MainWindow", "Год выпуска"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Режисер"))
        self.pushButton.setText(_translate("MainWindow", "Добавить запись "))
        self.label_5.setText(_translate("MainWindow", "Страна"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.load.setText(_translate("MainWindow", "Загрузить"))
        self.find.setText(_translate("MainWindow", "Поиск"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.delete_2.setText(_translate("MainWindow", "удалить"))
