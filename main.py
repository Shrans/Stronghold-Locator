from base64 import b64decode
import sys,os
import webbrowser
import pyperclip
 
from PySide6 import QtWidgets
from PySide6.QtWidgets import *

 
from qtgui_ui import Ui_MainWindow

from set_ui import Ui_Dialog

import LocatorLib,time,json,plt

import requests

from memory_pic import *


if not os.path.exists('icon.ico'):
    def get_pic(pic_code, pic_name):
        image = open(pic_name, 'wb')
        image.write(b64decode(pic_code))
        image.close()

    get_pic(icon_ico, 'icon.ico')


# 检查文件是否存在
if not os.path.exists('set.json'):
    # 如果文件不存在，则创建并写入初始内容
    data = {"debug": False, "debug_version": False, "map": True}
    with open('set.json', 'w') as f:
        json.dump(data, f)


tp = ""
version = "v3.0.0"
vc = vd = 0
with open("set.json","r") as f:
    set_json=json.loads(f.read())


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

class Dialog(QDialog):
    def __init__(self, parent = None) :
        with open("set.json","r") as f:
            out=json.loads(f.read())
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if not bool(out["debug"]):
            self.ui.tabWidget.removeTab(1)
        self.ui.debug_ver.setChecked(set_json["debug_version"])
        self.ui.open_map.setChecked(set_json["map"])
        self.ui.off_debug.clicked.connect(self.off_debug)
        self.ui.enter.clicked.connect(self.enter)
        self.ui.debug_ver.clicked.connect(self.debug_ver)
        self.ui.open_map.clicked.connect(self.open_map)

    
    def enter(self):
        with open("set.json","w") as f:
            f.write(json.dumps(set_json))
        QMessageBox.about(self,"重启应用程序","请重启本应用，以应用设置。")
        app.exit(app.exec())
        
    def off_debug(self):
        global set_json
        set_json["debug"]=False
        QMessageBox.about(self,"关闭调试模式","已关闭。")
    
    def debug_ver(self):
        global set_json
        set_json["debug_version"]=self.ui.debug_ver.isChecked()
    
    def open_map(self):
        global set_json
        set_json["map"]=self.ui.open_map.isChecked()
    
    



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
        self.ui.jc_gx.triggered.connect(self.jc_gx)
        self.ui.open_log.triggered.connect(self.open_log)
        self.ui.open_set.triggered.connect(self.open_set)
    

    def dx_jd(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        xyt_2=str(self.ui.xyt_2.text())
        out=LocatorLib.Calculate(xyt_1,xyt_2)
        if type(out)==str:
            self.ui.print_err.showMessage("错误："+out,5000)
            self.ui.out_x.setText("")
            self.ui.out_z.setText("")
            self.ui.out_tp.setText("")
            LogTxt(xyt_1,xyt_2,out)
        else:
            tp = out[2]
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])
            LogTxt(xyt_1,xyt_2,out)
            if set_json['map']:
                inxyt_1 = (float(str(self.ui.xyt_1.text()).split()[6]),float(str(self.ui.xyt_1.text()).split()[8]))
                inxyt_2 = (float(str(self.ui.xyt_2.text()).split()[6]),float(str(self.ui.xyt_2.text()).split()[8]))
                plt.plot_points_s(inxyt_1,inxyt_2,(int(out[0]),int(out[1])))
    def dx_gs(self):
        global tp
        xyt_1=str(self.ui.xyt_1.text())
        out=LocatorLib.Estimate(xyt_1)
        if type(out)==str:
            self.ui.print_err.showMessage("错误："+out,5000)
            self.ui.out_x.setText("")
            self.ui.out_z.setText("")
            self.ui.out_tp.setText("")
            LogTxt(xyt_1,"估算模式",out)
        else:
            tp = out[2]
            self.ui.out_x.setText(out[0])
            self.ui.out_z.setText(out[1])
            self.ui.out_tp.setText(out[2])
            LogTxt(xyt_1,"估算模式",out)
            if set_json['map']:
                inxyt = (float(str(self.ui.xyt_1.text()).split()[6]),float(str(self.ui.xyt_1.text()).split()[8]))
                plt.plot_points_t(inxyt,(int(out[0]),int(out[1])))


    def copy_tp(self):
        global tp
        pyperclip.copy(tp)
    
    def copy_1(self):
        self.ui.xyt_1.setText(pyperclip.paste())

    def copy_2(self):
        self.ui.xyt_2.setText(pyperclip.paste())
    
    def ck_y(self):
        global vd
        if vd < 3:
            webbrowser.open("https://github.com/Shrans/Stronghold-Locator")
            vd+=1
        else:
            with open("set.json","r") as f:
                set=json.loads(f.read())
                set["debug"] = True
            with open("set.json","w") as f:
                f.write(json.dumps(set))
                
            webbrowser.open("https://github.com/Shrans/Stronghold-Locator")
            QMessageBox.information(self, "调试模式", "已开启调试模式。\n请重启该程序")
            app.exit(app.exec())
        

    def bh_y(self):
        webbrowser.open("https://space.bilibili.com/228828764")
    
    def bh_g(self):
        webbrowser.open("https://space.bilibili.com/502594227")
    
    def open_log(self):
        os.system("start log.txt")
        # QMessageBox.information(self, "关于", "这是一个关于对话框",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    
    def open_set(self):
        with open("set.json","r") as f:
            global set_json
            set_json=json.loads(f.read())
        set.show()
    
    def jc_gx(self):

        global vc
        if not set_json["debug_version"]:
            response = requests.get("https://api.github.com/repos/Shrans/Stronghold-Locator/releases/latest")
            data = response.json()

        else:
            response = requests.get("https://api.github.com/repos/Shrans/Stronghold-Locator/releases")
            data = response.json()[0]


        tag_name = data["tag_name"]
        if version == tag_name:
            if vc < 2:
                QMessageBox.information(self, "检查更新", "你正在使用最新版")
                vc+=1
            else:
                QMessageBox.information(self, "检查更新", "你正在使用最新版\n不要频繁使用该功能！如使用频率过高，您将会被GitHub拒绝访问一段时间！")

        else:
            if QMessageBox.information(self, "发现新版本", f"你的版本：{version}，新的版本{data['tag_name']}\n新版本介绍：\n{data['body']}",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
                webbrowser.open(data["html_url"])

 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Stronghold-Locator-GUI")
    win.show()
    set = Dialog()
    set.setWindowTitle("Stronghold-Locator-GUI-SET")
    win.ui.print_err.showMessage("欢迎使用Stronghold-Locator-GUI应用程序")
    app.exit(app.exec())