# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

def say_hello():
    print("Button clicked, Hello!") #text_log

class Mew(QWidget):
    def __init__(self):
        super(Mew, self).__init__()
        self.load_ui()

    def test():
        print("Button clicked, Hello!") #text_log

    def ButtonClicked(self):
        self.label.setText("Bonjour "+self.Edit.text())


    def load_ui(self):
        loader = QUiLoader()
        self.btn_start.QtWidgets.QPushButton(self.centralwidget, clicked = Lambda: self.test())
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication([])
    widget = Mew()
    widget.show()
    sys.exit(app.exec_())
