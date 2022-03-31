# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QFile
from PyQt5.QtUiTools import QUiLoader

def say_hello():
    print("Button clicked, Hello!") #text_log

class Mew(QWidget):
    def __init__(self):
        super(Mew, self).__init__()
        self.load_ui()

    def button_clicked(self):
        print("Button clicked, Hello!") #text_log
        #self.text_log.setText("[17:30] - Start")


    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        self.btn_start = QtWidgets.QPushButton(self)
        #self.b1.setText("CLIQUEZ")
        self.btn_start.clicked.connect(self.button_clicked)

if __name__ == "__main__":
    app = QApplication([])
    widget = Mew()
    widget.show()
    sys.exit(app.exec_())
