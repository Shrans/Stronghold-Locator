import sys
import webbrowser
 
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
 
from qtgui_ui import Ui_MainWindow

import LocatorLib


class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dx_jd.clicked.connect(self.dx_jd)
        self.ui.dx_gs.clicked.connect(self.dx_gs)
        self.ui.about.clicked.connect(self.about)
    

    def dx_jd(self):
        xyt_1=str(self.ui.xyt_1.text())
        xyt_2=str(self.ui.xyt_2.text())
        self.ui.print_out.setText(LocatorLib.Calculate(xyt_1,xyt_2))

    def dx_gs(self):
        xyt_1=str(self.ui.xyt_1.text())
        self.ui.print_out.setText(LocatorLib.Estimate(xyt_1))

    def about():
        webbrowser.open("github.com/lidongxun967/Stronghold-Locator-GUI")

 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Stronghold-Locator")
    win.show()
    app.exit(app.exec_())