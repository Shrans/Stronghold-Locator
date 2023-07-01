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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(836, 316)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 2)

        self.dx_jd = QPushButton(self.centralwidget)
        self.dx_jd.setObjectName(u"dx_jd")
        self.dx_jd.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.dx_jd, 4, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.dx_gs = QPushButton(self.centralwidget)
        self.dx_gs.setObjectName(u"dx_gs")
        self.dx_gs.setEnabled(True)
        self.dx_gs.setMinimumSize(QSize(200, 0))
        self.dx_gs.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.dx_gs, 4, 1, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(30)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.about = QPushButton(self.centralwidget)
        self.about.setObjectName(u"about")
        self.about.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.about, 4, 5, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 4)

        self.print_out = QTextBrowser(self.centralwidget)
        self.print_out.setObjectName(u"print_out")

        self.gridLayout.addWidget(self.print_out, 1, 4, 3, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.copy_tp = QPushButton(self.centralwidget)
        self.copy_tp.setObjectName(u"copy_tp")
        self.copy_tp.setMinimumSize(QSize(200, 0))
        self.copy_tp.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.copy_tp, 4, 3, 1, 2)

        self.xyt_1 = QLineEdit(self.centralwidget)
        self.xyt_1.setObjectName(u"xyt_1")
        self.xyt_1.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.xyt_1, 1, 2, 1, 1)

        self.xyt_2 = QLineEdit(self.centralwidget)
        self.xyt_2.setObjectName(u"xyt_2")
        self.xyt_2.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.xyt_2, 2, 2, 1, 1)

        self.copy_1 = QPushButton(self.centralwidget)
        self.copy_1.setObjectName(u"copy_1")

        self.gridLayout.addWidget(self.copy_1, 1, 3, 1, 1)

        self.copy_2 = QPushButton(self.centralwidget)
        self.copy_2.setObjectName(u"copy_2")

        self.gridLayout.addWidget(self.copy_2, 2, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.print_out.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        self.xyt_1.raise_()
        self.xyt_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.dx_jd.raise_()
        self.dx_gs.raise_()
        self.about.raise_()
        self.label_4.raise_()
        self.copy_tp.raise_()
        self.copy_1.raise_()
        self.copy_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\uff1a", None))
        self.dx_jd.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u659c\u5f0f\u4ea4\u70b9\u6cd5\u8ba1\u7b97", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e2\uff08\u70b9\u659c\u5f0f\u4ea4\u70b9\u6cd5\u9700\u8981\uff09\uff1a", None))
        self.dx_gs.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u659c\u5f0f\u4f30\u7b97\u6cd5\u8ba1\u7b97", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stronghold-Locator", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u5730\u5740", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u25b2\u6ce8\u610f\uff1a\u70b9\u659c\u5f0f\u4f30\u7b97\u6cd5\u6682\u4e0d\u652f\u6301\u5bf9\u8d85\u51fa\u8ddd\u79bb\u4e3b\u4e16\u754c\u539f\u70b91728\u683c\u7684\u6570\u636e\u8fdb"
                        "\u884c\u4f30\u7b97</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e1\uff08\u59cb\u7ec8\u9700\u8981\uff09\uff1a", None))
        self.copy_tp.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236TP\u6307\u4ee4", None))
        self.copy_1.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u526a\u8d34\u677f", None))
        self.copy_2.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u526a\u8d34\u677f", None))
    # retranslateUi

