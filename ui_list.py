# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(715, 462)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(270, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_3.addWidget(self.textBrowser)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"uSearch - \u68c0\u7d22\u7ed3\u679c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6240\u6709\u7ed3\u679c", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"<\u767e\u5ea6\u767e\u79d1>", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Linux \u6559\u7a0b | \u83dc\u9e1f\u6559\u7a0b", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"Download Linux | Linux.org", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u9884\u89c8", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Linux\uff0c\u5168\u79f0GNU/Linux\uff0c\u662f\u4e00\u79cd\u514d\u8d39\u4f7f\u7528\u548c\u81ea\u7531\u4f20\u64ad\u7684\u7c7bUNIX\u64cd\u4f5c\u7cfb\u7edf\uff0c\u5176\u5185\u6838\u7531\u6797\u7eb3\u65af\u00b7\u672c\u7eb3\u7b2c\u514b\u7279\u00b7\u6258\u74e6\u5179\u4e8e1991\u5e7410\u67085\u65e5\u9996\u6b21\u53d1\u5e03\uff0c\u5b83\u4e3b\u8981\u53d7\u5230Minix\u548cUnix\u601d\u60f3\u7684\u542f\u53d1\uff0c\u662f\u4e00\u4e2a\u57fa\u4e8ePOSIX\u7684\u591a\u7528\u6237\u3001\u591a\u4efb\u52a1\u3001\u652f\u6301\u591a\u7ebf\u7a0b\u548c\u591aCPU\u7684\u64cd\u4f5c\u7cfb\u7edf\u3002"
                        "\u5b83\u80fd\u8fd0\u884c\u4e3b\u8981\u7684Unix\u5de5\u5177\u8f6f\u4ef6\u3001\u5e94\u7528\u7a0b\u5e8f\u548c\u7f51\u7edc\u534f\u8bae\u3002\u5b83\u652f\u630132\u4f4d\u548c64\u4f4d\u786c\u4ef6\u3002Linux\u7ee7\u627f\u4e86Unix\u4ee5\u7f51\u7edc\u4e3a\u6838\u5fc3\u7684\u8bbe\u8ba1\u601d\u60f3\uff0c\u662f\u4e00\u4e2a\u6027\u80fd\u7a33\u5b9a\u7684\u591a\u7528\u6237\u7f51\u7edc\u64cd\u4f5c\u7cfb\u7edf\u3002Linux\u6709\u4e0a\u767e\u79cd\u4e0d\u540c\u7684\u53d1\u884c\u7248\uff0c\u5982\u57fa\u4e8e\u793e\u533a\u5f00\u53d1\u7684debian\u3001archlinux\uff0c\u548c\u57fa\u4e8e\u5546\u4e1a\u5f00\u53d1\u7684Red Hat Enterprise Linux\u3001SUSE\u3001Oracle Linux\u7b49\u3002</p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u53c2\u8003\u94fe\u63a5", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"URL\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u5728\u9ed8\u8ba4\u6d4f\u89c8\u5668\u6253\u5f00", None))
    # retranslateUi

