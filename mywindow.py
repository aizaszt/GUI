from PyQt6.QtWidgets import QMessageBox,QLineEdit, QPushButton, QLabel, QMainWindow, QApplication
import os
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lineweight = QLineEdit(self)
        self.lineheight = QLineEdit(self)
        self.pushButton = QPushButton(self)

        ui_path = os.path.join(os.path.dirname(__file__), "bmi.ui")
        uic.loadUi(ui_path, self)
        self.pushButton.clicked.connect(self.on_click)


        self.actionExit.triggered.connect(QApplication.quit)
        self.actionClear.triggered.connect(self.clear)
        self.actionAbout.triggered.connect(self.info)
    def on_click(self):
        num1 = self.lineweight.text()
        num2 = self.lineheight.text()
        bmi = int(num1)/((int(num2)/100)**2)
        bmi1 = int(bmi)
        self.pushButton.setText('Your Body Mass Index: ' + str(bmi1))

        if bmi1 < 18:
            self.pushButton.setStyleSheet("background-color: rgb(255, 239, 161)")

        elif 18 < bmi1 < 25:
            self.pushButton.setStyleSheet("background-color:  rgb(111, 255, 128)")

        elif 25< bmi1 < 30:
            self.pushButton.setStyleSheet("background-color: rgb(255, 140, 101)")

        else:
            self.pushButton.setStyleSheet("background-color: rgb(171, 14, 14)")

    def clear(self):
        self.lineweight.clear()
        self.lineheight.clear()
        self.pushButton.setText("CALCULATE")
        self.pushButton.setStyleSheet("")

    def info(self):
        QMessageBox.information(self,'The Body Mass Index (BMI) Calculator can be used to ')
