import sys,os
import webbrowser
import pyperclip
 
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
 
from qtgui_ui import Ui_MainWindow

import LocatorLib,time

tp = ""

def LogTxt(xyt_1, xyt_2,out):
    with open("log.txt", "a",encoding = 'utf-8') as f:
        if type(out)==str:
            f.write(f"""

时间：{time.ctime()}
位置1：{xyt_1}
位置2：{xyt_2}
错误信息：{out}

""")
        else:
            f.write(f"""

时间：{time.ctime()}
位置1：{xyt_1}
位置2：{xyt_2}
结果：x={out[0]},y={out[1]}
TP指令：{out[2]}
""")

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
        self.ui.bh_y.triggered.connect(self.bh_y)
        self.ui.bh_g.triggered.connect(self.bh_g)
        self.ui.open_log.triggered.connect(self.open_log)
    

    def dx_jd(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        xyt_2=str(self.ui.xyt_2.text())
        out=LocatorLib.Calculate(xyt_1,xyt_2)
        if type(out)==str:
            self.ui.out_err.setText(out)
            self.ui.out_x.setText("")
            self.ui.out_z.setText("")
            self.ui.out_tp.setText("")
            LogTxt(xyt_1,xyt_2,out)
        else:
            tp = out[2]
            self.ui.out_err.setText("")
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])
            LogTxt(xyt_1,xyt_2,out)

    def dx_gs(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        out=LocatorLib.Estimate(xyt_1)
        if type(out)==str:
            self.ui.out_err.setText(out)
            self.ui.out_x.setText("")
            self.ui.out_z.setText("")
            self.ui.out_tp.setText("")
            LogTxt(xyt_1,"估算模式",out)
        else:
            tp = out[2]
            self.ui.out_err.setText("")
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])
            LogTxt(xyt_1,"估算模式",out)

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

    def bh_y(self):
        webbrowser.open("https://space.bilibili.com/228828764")
    
    def bh_g(self):
        webbrowser.open("https://space.bilibili.com/502594227")
    
    def open_log(self):
        os.system("start log.txt")



 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Stronghold-Locator-GUI")
    win.show()
    app.exit(app.exec_())