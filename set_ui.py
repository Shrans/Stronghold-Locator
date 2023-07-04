# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.exit = QPushButton(Dialog)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(310, 260, 75, 23))
        self.enter = QPushButton(Dialog)
        self.enter.setObjectName(u"enter")
        self.enter.setGeometry(QRect(230, 260, 75, 23))
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 9, 381, 241))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.open_map = QCheckBox(self.tab)
        self.open_map.setObjectName(u"open_map")
        self.open_map.setGeometry(QRect(10, 10, 101, 19))
        self.tabWidget.addTab(self.tab, "")
        self.debug_tab = QWidget()
        self.debug_tab.setObjectName(u"debug_tab")
        self.off_debug = QPushButton(self.debug_tab)
        self.off_debug.setObjectName(u"off_debug")
        self.off_debug.setGeometry(QRect(280, 190, 91, 23))
        self.debug_ver = QCheckBox(self.debug_tab)
        self.debug_ver.setObjectName(u"debug_ver")
        self.debug_ver.setGeometry(QRect(10, 10, 121, 19))
        self.tabWidget.addTab(self.debug_tab, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.exit.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.enter.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.open_map.setText(QCoreApplication.translate("Dialog", u"\u5f00\u542f\u7ed8\u56fe\u6a21\u5f0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u57fa\u7840", None))
        self.off_debug.setText(QCoreApplication.translate("Dialog", u"\u5173\u95ed\u8c03\u8bd5\u6a21\u5f0f", None))
        self.debug_ver.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u9884\u53d1\u5e03\u7248\u66f4\u65b0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debug_tab), QCoreApplication.translate("Dialog", u"\u8c03\u8bd5", None))
    # retranslateUi

