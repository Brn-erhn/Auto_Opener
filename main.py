# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import time
import os

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QScrollBar, QLabel, QTextBrowser, QTextEdit, \
    QLineEdit, QRadioButton, QFileDialog
from PyQt5 import uic, QtCore
import threading


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("AutoOpener.ui", self)
        self.openButton = self.findChild(QPushButton, "openButton")
        self.path = self.findChild(QLabel, "path")
        self.openButton.clicked.connect(self.open_file)
        self.label = self.findChild(QLabel, "label")

        self.hour = self.findChild(QRadioButton, "radioButton_2")
        self.second = self.findChild(QRadioButton, "radioButton")
        self.info = self.findChild(QTextEdit, "textEdit")
        self.openTimes = self.findChild(QLabel, "times")
        self.times = []

        self.show()

    def sleep(self, seconds, starter):
        while True:

            self.times.append(time.ctime())
            self.openTimes.setText(self.openTimes.text()+f"\nTimes opened: {self.times[-1]}")
            print("Times opened: ", self.times[-1])
            os.startfile(f"{starter}")
            time.sleep(seconds)

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.path.setText(fileName[0])
        print(fileName)
        if self.hour.isChecked():

            try:

                    # Start the file here

                    # Pause the program for 3 hours (3 * 60 * 60 seconds)
                    sleep_time = int(float(self.info.toPlainText())) * 60 * 60
                    t1 = threading.Thread(target=self.sleep, args=(sleep_time, fileName[0]))
                    t1.start()


            except:
                self.label.setText("Please enter a valid number. Like 1 or 2 or 3")


        elif self.second.isChecked():

            try:

                sleep_time = (int(float(self.info.toPlainText())))
                t1 = threading.Thread(target=self.sleep, args=(sleep_time, fileName[0]))
                t1.start()



            except:
                self.label.setText("Please enter a valid number. Like 1 or 2 or 3")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    UIWindow = Ui()
    app.exec_()
