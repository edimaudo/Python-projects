#pyQt skeleton code

import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "tax_calculator.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.price_input.toPlainText())
        tax = (self.tax_rate_input.value())
        total_price = price + ((tax/100)*price)
        total_price_output= "The total price with tax is: " + str(total_price)
        self.output_text.setText(total_price_output)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
