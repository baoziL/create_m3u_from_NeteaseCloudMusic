# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui',
# licensing of 'UI.ui' applies.
#
# Created: Thu Feb  7 15:44:06 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(694, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(main_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(main_window)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.folder_path = QtWidgets.QLineEdit(main_window)
        self.folder_path.setObjectName("folder_path")
        self.horizontalLayout.addWidget(self.folder_path)
        self.select_folder = QtWidgets.QPushButton(main_window)
        self.select_folder.setMaximumSize(QtCore.QSize(25, 16777215))
        self.select_folder.setObjectName("select_folder")
        self.horizontalLayout.addWidget(self.select_folder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.all_select_button = QtWidgets.QPushButton(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_select_button.sizePolicy().hasHeightForWidth())
        self.all_select_button.setSizePolicy(sizePolicy)
        self.all_select_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.all_select_button.setObjectName("all_select_button")
        self.horizontalLayout_2.addWidget(self.all_select_button)
        self.reverse_button = QtWidgets.QPushButton(main_window)
        self.reverse_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.reverse_button.setObjectName("reverse_button")
        self.horizontalLayout_2.addWidget(self.reverse_button)
        self.cancel_button = QtWidgets.QPushButton(main_window)
        self.cancel_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.list_button = QtWidgets.QPushButton(main_window)
        self.list_button.setObjectName("list_button")
        self.horizontalLayout_2.addWidget(self.list_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(main_window)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtWidgets.QApplication.translate("main_window", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("main_window", "歌单保存路径:", None, -1))
        self.select_folder.setText(QtWidgets.QApplication.translate("main_window", "...", None, -1))
        self.all_select_button.setText(QtWidgets.QApplication.translate("main_window", "全选", None, -1))
        self.reverse_button.setText(QtWidgets.QApplication.translate("main_window", "反选", None, -1))
        self.cancel_button.setText(QtWidgets.QApplication.translate("main_window", "取消", None, -1))
        self.list_button.setText(QtWidgets.QApplication.translate("main_window", "列出歌单", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("main_window", "歌单名", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("main_window", "歌曲数", None, -1))

