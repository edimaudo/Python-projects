#PyQT temperature converter
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "temperatureConverter.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.convertCF.clicked.connect(self.CtoF)
        self.convertFC.clicked.connect(self.FtoC)

    def CtoF(self):
        cel = self.celsiusInput.value()
        fahr = cel * 9 / 5.0 + 32
        self.farenheitInput.setValue(fahr)

    def FtoC(self):
        fahr = self.farenheitInput.value()
        cel = (fahr - 32)/1.8
        self.celsiusInput.setValue(cel)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
