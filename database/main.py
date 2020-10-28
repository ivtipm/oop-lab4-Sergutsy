from PyQt5 import QtWidgets, QtGui
from ui import Ui_MainWindow
import sys
from databass import *

db = Databass()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(("ID", "Название", "Режисер", "год выпуска", "Страна"))

        # добавление значений в комбо боксы
        self.ui.comboBox.addItems(("название", "режисер", "год", "страна"))
        self.ui.pole.addItems(("название", "режисер", "год", "страна"))

        # подключение кнопочек
        self.ui.save.clicked.connect(self.saveClicked)
        self.ui.load.clicked.connect(self.loadClicked)
        self.ui.change.clicked.connect(self.changeClicked)
        self.ui.find.clicked.connect(self.findClicked)
        self.ui.delete_2.clicked.connect(self.deleteClicked)
        self.ui.pushButton.clicked.connect(self.addClicked)

    def saveClicked(self):
        db.save()

    def loadClicked(self):
        db.load()
        self.ui.tableWidget.setRowCount(len(db.get_id()))
        for i in db.get_id():
            self.ui.id.addItem(str(i))
            self.ui.id_2.addItem(str(i))

        for i in range(len(db.get_id())):
            info = QtWidgets.QTableWidgetItem(str(db.get_id()[i]))
            self.ui.tableWidget.setItem(i, 0, info)
            info = QtWidgets.QTableWidgetItem(db.get_name()[i])
            self.ui.tableWidget.setItem(i, 1, info)
            info = QtWidgets.QTableWidgetItem(db.get_rej()[i])
            self.ui.tableWidget.setItem(i, 2, info)
            info = QtWidgets.QTableWidgetItem(db.get_year()[i])
            self.ui.tableWidget.setItem(i, 3, info)
            info = QtWidgets.QTableWidgetItem(db.get_country()[i])
            self.ui.tableWidget.setItem(i, 4, info)
            for j in range(5):
                self.ui.tableWidget.item(i, j).setBackground(QtGui.QColor(255, 255, 255))

    def changeClicked(self):
        id = int(self.ui.id.currentText())
        pole = self.ui.pole.currentText()
        print(pole)
        word = self.ui.word.text()
        print(word)
        db.change(id, pole, word)
        self.ui.id.clear()
        self.ui.id_2.clear()
        self.loadClicked()

    def findClicked(self):
        for i in range(len(db.get_id())):
            for j in range(5):
                self.ui.tableWidget.item(i, j).setBackground(QtGui.QColor(255, 255, 255))
        pole = self.ui.comboBox.currentText()
        word = self.ui.lineEdit.text()
        id = db.find(pole, word)
        for i in range(5):
            self.ui.tableWidget.item(id, i).setBackground(QtGui.QColor(0, 0, 255))

    def deleteClicked(self):
        id = int(self.ui.id_2.currentText())
        db.delete(id)
        self.ui.id.clear()
        self.ui.id_2.clear()
        self.loadClicked()

    def addClicked(self):
        name = self.ui.Name.text()
        rej = self.ui.Rej.text()
        year = self.ui.Year.text()
        country = self.ui.Country.text()
        db.append(name, rej, year, country)
        self.ui.Name.clear()
        self.ui.Rej.clear()
        self.ui.Year.clear()
        self.ui.Country.clear()
        self.ui.id.clear()
        self.ui.id_2.clear()
        self.loadClicked()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())