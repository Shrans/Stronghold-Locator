# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtgui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(949, 295)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.ck_y = QAction(MainWindow)
        self.ck_y.setObjectName(u"ck_y")
        self.ck_gui = QAction(MainWindow)
        self.ck_gui.setObjectName(u"ck_gui")
        self.open_log = QAction(MainWindow)
        self.open_log.setObjectName(u"open_log")
        self.bh_y = QAction(MainWindow)
        self.bh_y.setObjectName(u"bh_y")
        self.bh_g = QAction(MainWindow)
        self.bh_g.setObjectName(u"bh_g")
        self.jc_gx = QAction(MainWindow)
        self.jc_gx.setObjectName(u"jc_gx")
        self.open_set = QAction(MainWindow)
        self.open_set.setObjectName(u"open_set")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.out_x = QLineEdit(self.centralwidget)
        self.out_x.setObjectName(u"out_x")
        self.out_x.setMinimumSize(QSize(100, 0))
        self.out_x.setMaximumSize(QSize(133, 16777215))
        self.out_x.setReadOnly(True)

        self.gridLayout.addWidget(self.out_x, 1, 25, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 24, 1, 1)

        self.copy_tp = QPushButton(self.centralwidget)
        self.copy_tp.setObjectName(u"copy_tp")
        self.copy_tp.setMinimumSize(QSize(0, 0))
        self.copy_tp.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.copy_tp, 2, 28, 1, 1)

        self.out_tp = QLineEdit(self.centralwidget)
        self.out_tp.setObjectName(u"out_tp")
        self.out_tp.setReadOnly(True)

        self.gridLayout.addWidget(self.out_tp, 2, 25, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.dx_gs = QPushButton(self.centralwidget)
        self.dx_gs.setObjectName(u"dx_gs")
        self.dx_gs.setEnabled(True)
        self.dx_gs.setMinimumSize(QSize(0, 0))
        self.dx_gs.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.dx_gs, 4, 24, 1, 5)

        self.xyt_1 = QLineEdit(self.centralwidget)
        self.xyt_1.setObjectName(u"xyt_1")
        self.xyt_1.setMinimumSize(QSize(315, 0))

        self.gridLayout.addWidget(self.xyt_1, 1, 2, 1, 1)

        self.copy_3 = QPushButton(self.centralwidget)
        self.copy_3.setObjectName(u"copy_3")

        self.gridLayout.addWidget(self.copy_3, 3, 6, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.xyt_2 = QLineEdit(self.centralwidget)
        self.xyt_2.setObjectName(u"xyt_2")
        self.xyt_2.setMinimumSize(QSize(315, 0))

        self.gridLayout.addWidget(self.xyt_2, 2, 2, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 4, 0, 3, 7)

        self.xyt_3 = QLineEdit(self.centralwidget)
        self.xyt_3.setObjectName(u"xyt_3")

        self.gridLayout.addWidget(self.xyt_3, 3, 2, 1, 1)

        self.out_z = QLineEdit(self.centralwidget)
        self.out_z.setObjectName(u"out_z")
        self.out_z.setMinimumSize(QSize(100, 0))
        self.out_z.setMaximumSize(QSize(200, 16777215))
        self.out_z.setReadOnly(True)

        self.gridLayout.addWidget(self.out_z, 1, 27, 1, 2)

        self.copy_2 = QPushButton(self.centralwidget)
        self.copy_2.setObjectName(u"copy_2")
        self.copy_2.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.copy_2, 2, 6, 1, 1)

        self.copy_1 = QPushButton(self.centralwidget)
        self.copy_1.setObjectName(u"copy_1")
        self.copy_1.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.copy_1, 1, 6, 1, 1)

        self.dx_sj = QPushButton(self.centralwidget)
        self.dx_sj.setObjectName(u"dx_sj")

        self.gridLayout.addWidget(self.dx_sj, 5, 24, 1, 5)

        self.dx_jd = QPushButton(self.centralwidget)
        self.dx_jd.setObjectName(u"dx_jd")
        self.dx_jd.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.dx_jd, 3, 24, 1, 5)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(10, 0))
        self.label_5.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.label_5, 1, 26, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(10, 0))
        self.label_4.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.label_4, 1, 24, 1, 1, Qt.AlignRight)

        self.win_top = QCheckBox(self.centralwidget)
        self.win_top.setObjectName(u"win_top")

        self.gridLayout.addWidget(self.win_top, 6, 27, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.textBrowser.raise_()
        self.xyt_1.raise_()
        self.copy_1.raise_()
        self.label_5.raise_()
        self.out_x.raise_()
        self.label_4.raise_()
        self.out_z.raise_()
        self.label_2.raise_()
        self.xyt_3.raise_()
        self.copy_3.raise_()
        self.xyt_2.raise_()
        self.copy_2.raise_()
        self.label_6.raise_()
        self.out_tp.raise_()
        self.copy_tp.raise_()
        self.dx_jd.raise_()
        self.dx_gs.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.dx_sj.raise_()
        self.win_top.raise_()
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 949, 21))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.print_err = QStatusBar(MainWindow)
        self.print_err.setObjectName(u"print_err")
        MainWindow.setStatusBar(self.print_err)

        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.ck_y)
        self.menu.addSeparator()
        self.menu.addAction(self.bh_y)
        self.menu.addAction(self.bh_g)
        self.menu.addAction(self.jc_gx)
        self.menu_2.addAction(self.open_log)
        self.menu_3.addAction(self.open_set)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ck_y.setText(QCoreApplication.translate("MainWindow", u"Github\u4ed3\u5e93", None))
        self.ck_gui.setText(QCoreApplication.translate("MainWindow", u"\u672cGUI\u7248\u4ed3\u5e93", None))
        self.open_log.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u65e5\u5fd7\u6587\u4ef6", None))
        self.bh_y.setText(QCoreApplication.translate("MainWindow", u"\u539f\u4f5c\u8005B\u7ad9\u4e3b\u9875", None))
        self.bh_g.setText(QCoreApplication.translate("MainWindow", u"GUI\u4f5c\u8005B\u7ad9\u4e3b\u9875", None))
        self.jc_gx.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.open_set.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TP\u6307\u4ee4\uff1a", None))
        self.copy_tp.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e1\uff08\u59cb\u7ec8\u9700\u8981\uff09\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stronghold-Locator-GUI", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e3\uff08\u4ec5\u4e09\u4ea4\u6cd5\u9700\u8981\uff09\uff1a", None))
        self.dx_gs.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u659c\u5f0f\u4f30\u7b97\u6cd5\u8ba1\u7b97", None))
        self.copy_3.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u526a\u8d34\u677f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e2\uff08\u4ec5\u4f30\u7b97\u6cd5\u4e0d\u9700\u8981\uff09\uff1a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u25cf\u4f7f\u7528\u65b9\u6cd5\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u2460\u5148\u5728\u6e38\u620f\u4e2d\u786e\u5b9a\u672b\u5f71\u4e4b\u773c\u7684\u65b9\u5411</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u2461\u6309\u4e0bF3+C\u590d\u5236\u5f53\u524d\u73a9\u5bb6\u4f4d\u7f6e\u4fe1\u606f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u2462\u5c06\u73a9\u5bb6\u4f4d\u7f6e\u4fe1\u606f\u7c98\u8d34\u5230\u6307\u5b9a\u7684\u8f93\u5165\u6846\u4e2d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u2463\u83b7\u53d6\u7ed3\u679c\u5750\u6807</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u25b2\u6ce8\u610f\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:12pt;\">\u2460\u70b9\u659c\u5f0f\u4f30\u7b97\u6cd5\u6682\u4e0d\u652f\u6301\u5bf9\u8d85\u51fa\u8ddd\u79bb\u4e3b\u4e16\u754c\u539f\u70b91728\u683c\u7684\u6570\u636e\u8fdb\u884c\u4f30\u7b97</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u2461\u5728\u8bb0\u5f55\u6570\u636e\u524d\u8bf7\u4fdd\u8bc1\u4e24\u4e2a\u672b\u5f71\u4e4b\u773c\u6307\u5411\u7684\u662f\u540c\u4e00\u4e2a\u8981\u585e</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.copy_2.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u526a\u8d34\u677f", None))
        self.copy_1.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u526a\u8d34\u677f", None))
        self.dx_sj.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u659c\u5f0f\u4e09\u4ea4\u6cd5\u8ba1\u7b97", None))
        self.dx_jd.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u659c\u5f0f\u4ea4\u70b9\u6cd5\u8ba1\u7b97", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X\uff1a", None))
        self.win_top.setText(QCoreApplication.translate("MainWindow", u"\u59cb\u7ec8\u7f6e\u9876", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u8bb0\u5f55", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u901a\u7528", None))
    # retranslateUi

