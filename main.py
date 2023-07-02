import sys
import webbrowser
import pyperclip
 
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
        self.ui.copy_1.clicked.connect(self.copy_1)
        self.ui.copy_2.clicked.connect(self.copy_2)
        self.ui.copy_tp.clicked.connect(self.copy_tp)
        self.ui.ck_y.triggered.connect(self.ck_y)
        self.ui.ck_gui.triggered.connect(self.ck_gui)
    

    def dx_jd(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        xyt_2=str(self.ui.xyt_2.text())
        out=LocatorLib.Calculate(xyt_1,xyt_2)
        if type(out)==str:
            self.ui.out_err.setText(out)
        else:
            tp = out[2]
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])

    def dx_gs(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        out=LocatorLib.Estimate(xyt_1)
        if type(out)==str:
            self.ui.out_err.setText(out)
        else:
            tp = out[2]
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])

    def about(self):
        webbrowser.open("github.com/lidongxun967/Stronghold-Locator-GUI")

    def copy_tp(self):
        global tp
        pyperclip.copy(tp)
    
    def copy_1(self):
        self.ui.xyt_1.setText(pyperclip.paste())

    def copy_2(self):
        self.ui.xyt_2.setText(pyperclip.paste())
    
    def ck_y(self):
        webbrowser.open("https://github.com/Shrans/Stronghold-Locator")

    def ck_gui(self):
        webbrowser.open("https://github.com/lidongxun967/Stronghold-Locator-GUI")
    




 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Stronghold-Locator-GUI")
    win.show()
    app.exit(app.exec_())