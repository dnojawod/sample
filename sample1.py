import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)

    window1 = QtWidgets.QWidget()

    window1.setWindowTitle("Sample Code")

    window1.setGeometry(50, 50, 500, 500)

    window1.show()

    sys.exc_info(app.exec())

window()