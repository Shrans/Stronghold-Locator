import sys
import webbrowser
from pyperclip import copy
 
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
 
from qtgui_ui import Ui_MainWindow

import LocatorLib

tp = ""


class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dx_jd.clicked.connect(self.dx_jd)
        self.ui.dx_gs.clicked.connect(self.dx_gs)
        self.ui.about.clicked.connect(self.about)
        self.ui.copy_tp.clicked.connect(self.copy_tp)
    

    def dx_jd(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        xyt_2=str(self.ui.xyt_2.text())
        out=LocatorLib.Calculate(xyt_1,xyt_2)
        if type(out)==str:
            self.ui.print_out.setText(out)
        else:
            tp = out[1]
            self.ui.print_out.setText(out[0]+out[1]+'(y轴坐标可适当修改)')

    def dx_gs(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        out=LocatorLib.Estimate(xyt_1)
        if type(out)==str:
            self.ui.print_out.setText(out)
        else:
            tp = out[1]
            self.ui.print_out.setText(out[0]+out[1]+'(y轴坐标可适当修改)')

    def about(self):
        webbrowser.open("github.com/lidongxun967/Stronghold-Locator-GUI")

    def copy_tp(self):
        global tp
        copy(tp)



 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Stronghold-Locator")
    win.show()
    app.exit(app.exec_())