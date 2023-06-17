# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AbqJobsSubmitter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AbqJobsSubmitter(object):
    def setupUi(self, AbqJobsSubmitter):
        AbqJobsSubmitter.setObjectName("AbqJobsSubmitter")
        AbqJobsSubmitter.resize(478, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AbqJobsSubmitter.sizePolicy().hasHeightForWidth())
        AbqJobsSubmitter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        AbqJobsSubmitter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AbqJobsSubmitter.setWindowIcon(icon)
        self.lineEdit_InputFolder = QtWidgets.QLineEdit(AbqJobsSubmitter)
        self.lineEdit_InputFolder.setGeometry(QtCore.QRect(20, 20, 310, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_InputFolder.sizePolicy().hasHeightForWidth())
        self.lineEdit_InputFolder.setSizePolicy(sizePolicy)
        self.lineEdit_InputFolder.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_InputFolder.setObjectName("lineEdit_InputFolder")
        self.pushButton_selectInputFolder = QtWidgets.QPushButton(AbqJobsSubmitter)
        self.pushButton_selectInputFolder.setGeometry(QtCore.QRect(340, 20, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_selectInputFolder.sizePolicy().hasHeightForWidth())
        self.pushButton_selectInputFolder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_selectInputFolder.setFont(font)
        self.pushButton_selectInputFolder.setObjectName("pushButton_selectInputFolder")
        self.checkBox_delete = QtWidgets.QCheckBox(AbqJobsSubmitter)
        self.checkBox_delete.setGeometry(QtCore.QRect(20, 115, 420, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.checkBox_delete.setFont(font)
        self.checkBox_delete.setChecked(True)
        self.checkBox_delete.setTristate(False)
        self.checkBox_delete.setObjectName("checkBox_delete")
        self.label_CPUs = QtWidgets.QLabel(AbqJobsSubmitter)
        self.label_CPUs.setGeometry(QtCore.QRect(200, 70, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_CPUs.setFont(font)
        self.label_CPUs.setObjectName("label_CPUs")
        self.spinBox_cpusNum = QtWidgets.QSpinBox(AbqJobsSubmitter)
        self.spinBox_cpusNum.setGeometry(QtCore.QRect(260, 70, 60, 30))
        self.spinBox_cpusNum.setPrefix("")
        self.spinBox_cpusNum.setMaximum(64)
        self.spinBox_cpusNum.setProperty("value", 8)
        self.spinBox_cpusNum.setObjectName("spinBox_cpusNum")
        self.label_Abq_ver = QtWidgets.QLabel(AbqJobsSubmitter)
        self.label_Abq_ver.setGeometry(QtCore.QRect(20, 70, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.label_Abq_ver.setFont(font)
        self.label_Abq_ver.setObjectName("label_Abq_ver")
        self.lineEdit_AbqVer = QtWidgets.QLineEdit(AbqJobsSubmitter)
        self.lineEdit_AbqVer.setGeometry(QtCore.QRect(100, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.lineEdit_AbqVer.setFont(font)
        self.lineEdit_AbqVer.setCursorPosition(6)
        self.lineEdit_AbqVer.setObjectName("lineEdit_AbqVer")
        self.label_Expect = QtWidgets.QLabel(AbqJobsSubmitter)
        self.label_Expect.setGeometry(QtCore.QRect(20, 150, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.label_Expect.setFont(font)
        self.label_Expect.setObjectName("label_Expect")
        self.layoutWidget = QtWidgets.QWidget(AbqJobsSubmitter)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 150, 348, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.HLayout_fileType_checkBoxes = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.HLayout_fileType_checkBoxes.setContentsMargins(0, 2, 0, 2)
        self.HLayout_fileType_checkBoxes.setSpacing(10)
        self.HLayout_fileType_checkBoxes.setObjectName("HLayout_fileType_checkBoxes")
        self.checkBox_STA = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_STA.setEnabled(True)
        self.checkBox_STA.setObjectName("checkBox_STA")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_STA)
        self.checkBox_LOG = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_LOG.setEnabled(True)
        self.checkBox_LOG.setObjectName("checkBox_LOG")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_LOG)
        self.checkBox_MSG = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_MSG.setEnabled(True)
        self.checkBox_MSG.setObjectName("checkBox_MSG")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_MSG)
        self.checkBox_DAT = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_DAT.setEnabled(True)
        self.checkBox_DAT.setObjectName("checkBox_DAT")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_DAT)
        self.checkBox_RES = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_RES.setEnabled(True)
        self.checkBox_RES.setObjectName("checkBox_RES")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_RES)
        self.checkBox_STT = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_STT.setEnabled(True)
        self.checkBox_STT.setObjectName("checkBox_STT")
        self.HLayout_fileType_checkBoxes.addWidget(self.checkBox_STT)
        self.pushButton_Submit = QtWidgets.QPushButton(AbqJobsSubmitter)
        self.pushButton_Submit.setGeometry(QtCore.QRect(130, 200, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_Submit.setFont(font)
        self.pushButton_Submit.setObjectName("pushButton_Submit")
        self.pushButton_Close = QtWidgets.QPushButton(AbqJobsSubmitter)
        self.pushButton_Close.setGeometry(QtCore.QRect(260, 200, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.pushButton_Close.setFont(font)
        self.pushButton_Close.setObjectName("pushButton_Close")

        self.retranslateUi(AbqJobsSubmitter)
        self.lineEdit_InputFolder.editingFinished.connect(AbqJobsSubmitter.handleEditInpFolder) # type: ignore
        self.pushButton_selectInputFolder.clicked.connect(AbqJobsSubmitter.handleSelectInpFolder) # type: ignore
        self.lineEdit_AbqVer.editingFinished.connect(AbqJobsSubmitter.handleEditAbqVer) # type: ignore
        self.spinBox_cpusNum.valueChanged['int'].connect(AbqJobsSubmitter.handleEditCPUnums) # type: ignore
        self.checkBox_delete.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleDeleteFiles) # type: ignore
        self.checkBox_STA.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_STA) # type: ignore
        self.checkBox_LOG.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_LOG) # type: ignore
        self.checkBox_MSG.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_MSG) # type: ignore
        self.checkBox_DAT.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_DAT) # type: ignore
        self.checkBox_RES.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_RES) # type: ignore
        self.checkBox_STT.stateChanged['int'].connect(AbqJobsSubmitter.handleToggleFileType_STT) # type: ignore
        self.pushButton_Submit.clicked.connect(AbqJobsSubmitter.handleSubmit) # type: ignore
        self.pushButton_Close.clicked.connect(AbqJobsSubmitter.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AbqJobsSubmitter)
        AbqJobsSubmitter.setTabOrder(self.lineEdit_InputFolder, self.pushButton_selectInputFolder)
        AbqJobsSubmitter.setTabOrder(self.pushButton_selectInputFolder, self.lineEdit_AbqVer)
        AbqJobsSubmitter.setTabOrder(self.lineEdit_AbqVer, self.spinBox_cpusNum)
        AbqJobsSubmitter.setTabOrder(self.spinBox_cpusNum, self.checkBox_delete)
        AbqJobsSubmitter.setTabOrder(self.checkBox_delete, self.checkBox_STA)
        AbqJobsSubmitter.setTabOrder(self.checkBox_STA, self.checkBox_LOG)
        AbqJobsSubmitter.setTabOrder(self.checkBox_LOG, self.checkBox_MSG)
        AbqJobsSubmitter.setTabOrder(self.checkBox_MSG, self.checkBox_DAT)
        AbqJobsSubmitter.setTabOrder(self.checkBox_DAT, self.checkBox_RES)
        AbqJobsSubmitter.setTabOrder(self.checkBox_RES, self.checkBox_STT)

    def retranslateUi(self, AbqJobsSubmitter):
        _translate = QtCore.QCoreApplication.translate
        AbqJobsSubmitter.setWindowTitle(_translate("AbqJobsSubmitter", "AbqJobsSubmitter"))
        self.lineEdit_InputFolder.setPlaceholderText(_translate("AbqJobsSubmitter", "Input Folder"))
        self.pushButton_selectInputFolder.setText(_translate("AbqJobsSubmitter", "Select folder"))
        self.checkBox_delete.setText(_translate("AbqJobsSubmitter", "Delete other files after the calculation is completed"))
        self.label_CPUs.setText(_translate("AbqJobsSubmitter", "CPUs:"))
        self.label_Abq_ver.setText(_translate("AbqJobsSubmitter", "Abq ver:"))
        self.lineEdit_AbqVer.setText(_translate("AbqJobsSubmitter", "abaqus"))
        self.label_Expect.setText(_translate("AbqJobsSubmitter", "Expect:"))
        self.checkBox_STA.setText(_translate("AbqJobsSubmitter", "sta"))
        self.checkBox_LOG.setText(_translate("AbqJobsSubmitter", "log"))
        self.checkBox_MSG.setText(_translate("AbqJobsSubmitter", "msg"))
        self.checkBox_DAT.setText(_translate("AbqJobsSubmitter", "dat"))
        self.checkBox_RES.setText(_translate("AbqJobsSubmitter", "res"))
        self.checkBox_STT.setText(_translate("AbqJobsSubmitter", "stt"))
        self.pushButton_Submit.setText(_translate("AbqJobsSubmitter", "Submit"))
        self.pushButton_Close.setText(_translate("AbqJobsSubmitter", "Close"))
