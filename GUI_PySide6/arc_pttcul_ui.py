# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arc_pttcul.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QPlainTextEdit,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(799, 572)
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(210, 10, 581, 551))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 191, 451))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 19, 171, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PB_init = QPushButton(self.verticalLayoutWidget)
        self.PB_init.setObjectName(u"PB_init")
        font = QFont()
        font.setPointSize(12)
        self.PB_init.setFont(font)

        self.verticalLayout.addWidget(self.PB_init)

        self.PB_CCT_update = QPushButton(self.verticalLayoutWidget)
        self.PB_CCT_update.setObjectName(u"PB_CCT_update")
        self.PB_CCT_update.setFont(font)

        self.verticalLayout.addWidget(self.PB_CCT_update)

        self.PB_UDT_list = QPushButton(self.verticalLayoutWidget)
        self.PB_UDT_list.setObjectName(u"PB_UDT_list")
        self.PB_UDT_list.setFont(font)

        self.verticalLayout.addWidget(self.PB_UDT_list)

        self.PB_UDT_update = QPushButton(self.verticalLayoutWidget)
        self.PB_UDT_update.setObjectName(u"PB_UDT_update")
        self.PB_UDT_update.setFont(font)

        self.verticalLayout.addWidget(self.PB_UDT_update)

        self.PB_UDT_add = QPushButton(self.verticalLayoutWidget)
        self.PB_UDT_add.setObjectName(u"PB_UDT_add")
        self.PB_UDT_add.setFont(font)

        self.verticalLayout.addWidget(self.PB_UDT_add)

        self.PB_b30 = QPushButton(self.verticalLayoutWidget)
        self.PB_b30.setObjectName(u"PB_b30")
        self.PB_b30.setFont(font)

        self.verticalLayout.addWidget(self.PB_b30)

        self.PB_r10 = QPushButton(self.verticalLayoutWidget)
        self.PB_r10.setObjectName(u"PB_r10")
        self.PB_r10.setFont(font)

        self.verticalLayout.addWidget(self.PB_r10)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 460, 191, 101))
        self.output_text = QPlainTextEdit(self.groupBox_2)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setGeometry(QRect(10, 20, 171, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u64cd\u4f5c", None))
        self.PB_init.setText(QCoreApplication.translate("Form", u"\n"
"\u521d\u59cb\u5316\n"
"", None))
        self.PB_CCT_update.setText(QCoreApplication.translate("Form", u"\n"
"\u66f4\u65b0\u5b9a\u6570\u8868\n"
"", None))
        self.PB_UDT_list.setText(QCoreApplication.translate("Form", u"\n"
"\u5217\u51fa\u7528\u6237\u6210\u7ee9\n"
"", None))
        self.PB_UDT_update.setText(QCoreApplication.translate("Form", u"\n"
"\u66f4\u65b0\u73b0\u6709\u6210\u7ee9\n"
"", None))
        self.PB_UDT_add.setText(QCoreApplication.translate("Form", u"\n"
"\u6dfb\u52a0\u65b0\u6210\u7ee9\n"
"", None))
        self.PB_b30.setText(QCoreApplication.translate("Form", u"\n"
"\u8ba1\u7b97b30\n"
"", None))
        self.PB_r10.setText(QCoreApplication.translate("Form", u"\n"
"\u8ba1\u7b97r10\n"
"", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.output_text.setPlainText("")
    # retranslateUi

