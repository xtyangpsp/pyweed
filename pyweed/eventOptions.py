# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 520)
        Dialog.setMinimumSize(QtCore.QSize(320, 520))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timeGroupBox = QtGui.QGroupBox(Dialog)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.timeGroupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.startDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.startDateTimeEdit.setObjectName(_fromUtf8("startDateTimeEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.startDateTimeEdit)
        self.startTimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.startTimeLabel.setObjectName(_fromUtf8("startTimeLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.startTimeLabel)
        self.endDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        self.endDateTimeEdit.setObjectName(_fromUtf8("endDateTimeEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.endDateTimeEdit)
        self.endTimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.endTimeLabel.setObjectName(_fromUtf8("endTimeLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.endTimeLabel)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.magDepthGroupBox = QtGui.QGroupBox(Dialog)
        self.magDepthGroupBox.setObjectName(_fromUtf8("magDepthGroupBox"))
        self.gridLayout = QtGui.QGridLayout(self.magDepthGroupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.maximumDepthLineEdit = QtGui.QLineEdit(self.magDepthGroupBox)
        self.maximumDepthLineEdit.setObjectName(_fromUtf8("maximumDepthLineEdit"))
        self.gridLayout.addWidget(self.maximumDepthLineEdit, 6, 2, 1, 1)
        self.minimumDepthLineEdit = QtGui.QLineEdit(self.magDepthGroupBox)
        self.minimumDepthLineEdit.setObjectName(_fromUtf8("minimumDepthLineEdit"))
        self.gridLayout.addWidget(self.minimumDepthLineEdit, 6, 1, 1, 1)
        self.depthBoxLabel = QtGui.QLabel(self.magDepthGroupBox)
        self.depthBoxLabel.setObjectName(_fromUtf8("depthBoxLabel"))
        self.gridLayout.addWidget(self.depthBoxLabel, 6, 0, 1, 1)
        self.maximumMagnitudeLineEdit = QtGui.QLineEdit(self.magDepthGroupBox)
        self.maximumMagnitudeLineEdit.setObjectName(_fromUtf8("maximumMagnitudeLineEdit"))
        self.gridLayout.addWidget(self.maximumMagnitudeLineEdit, 2, 2, 1, 1)
        self.minimumMagnitudLineEdit = QtGui.QLineEdit(self.magDepthGroupBox)
        self.minimumMagnitudLineEdit.setObjectName(_fromUtf8("minimumMagnitudLineEdit"))
        self.gridLayout.addWidget(self.minimumMagnitudLineEdit, 2, 1, 1, 1)
        self.magnitudeBoxLabel = QtGui.QLabel(self.magDepthGroupBox)
        self.magnitudeBoxLabel.setObjectName(_fromUtf8("magnitudeBoxLabel"))
        self.gridLayout.addWidget(self.magnitudeBoxLabel, 2, 0, 1, 1)
        self.minimumBoxLabel = QtGui.QLabel(self.magDepthGroupBox)
        self.minimumBoxLabel.setObjectName(_fromUtf8("minimumBoxLabel"))
        self.gridLayout.addWidget(self.minimumBoxLabel, 1, 1, 1, 1)
        self.maximumBoxLabel = QtGui.QLabel(self.magDepthGroupBox)
        self.maximumBoxLabel.setObjectName(_fromUtf8("maximumBoxLabel"))
        self.gridLayout.addWidget(self.maximumBoxLabel, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.magDepthGroupBox)
        self.catalogTypeGroupBox = QtGui.QGroupBox(Dialog)
        self.catalogTypeGroupBox.setObjectName(_fromUtf8("catalogTypeGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.catalogTypeGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cataloComboBox = QtGui.QComboBox(self.catalogTypeGroupBox)
        self.cataloComboBox.setObjectName(_fromUtf8("cataloComboBox"))
        self.cataloComboBox.addItem(_fromUtf8(""))
        self.cataloComboBox.addItem(_fromUtf8(""))
        self.cataloComboBox.addItem(_fromUtf8(""))
        self.cataloComboBox.addItem(_fromUtf8(""))
        self.cataloComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cataloComboBox, 1, 0, 1, 1)
        self.typeComboBox = QtGui.QComboBox(self.catalogTypeGroupBox)
        self.typeComboBox.setObjectName(_fromUtf8("typeComboBox"))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.typeComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.typeComboBox, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.catalogTypeGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(Dialog)
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.locationGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.eastValue = QtGui.QLineEdit(self.locationGroupBox)
        self.eastValue.setObjectName(_fromUtf8("eastValue"))
        self.gridLayout_3.addWidget(self.eastValue, 2, 0, 1, 1)
        self.westValue = QtGui.QLineEdit(self.locationGroupBox)
        self.westValue.setObjectName(_fromUtf8("westValue"))
        self.gridLayout_3.addWidget(self.westValue, 2, 2, 1, 1)
        self.centerLabel = QtGui.QLabel(self.locationGroupBox)
        self.centerLabel.setObjectName(_fromUtf8("centerLabel"))
        self.gridLayout_3.addWidget(self.centerLabel, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.northValue = QtGui.QLineEdit(self.locationGroupBox)
        self.northValue.setObjectName(_fromUtf8("northValue"))
        self.gridLayout_3.addWidget(self.northValue, 0, 1, 1, 1)
        self.southValue = QtGui.QLineEdit(self.locationGroupBox)
        self.southValue.setObjectName(_fromUtf8("southValue"))
        self.gridLayout_3.addWidget(self.southValue, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.locationGroupBox)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.timeGroupBox.setTitle(_translate("Dialog", "Event Time Interval", None))
        self.startTimeLabel.setText(_translate("Dialog", "Start Time", None))
        self.endTimeLabel.setText(_translate("Dialog", "End Time", None))
        self.magDepthGroupBox.setTitle(_translate("Dialog", "Magnitude and Depth", None))
        self.maximumDepthLineEdit.setText(_translate("Dialog", "6371.0", None))
        self.minimumDepthLineEdit.setText(_translate("Dialog", "0.0", None))
        self.depthBoxLabel.setText(_translate("Dialog", "Depth", None))
        self.maximumMagnitudeLineEdit.setText(_translate("Dialog", "10.0", None))
        self.minimumMagnitudLineEdit.setText(_translate("Dialog", "0.0", None))
        self.magnitudeBoxLabel.setText(_translate("Dialog", "Magnitude", None))
        self.minimumBoxLabel.setText(_translate("Dialog", "Minimum", None))
        self.maximumBoxLabel.setText(_translate("Dialog", "Maximum", None))
        self.catalogTypeGroupBox.setTitle(_translate("Dialog", "Catalog and Type", None))
        self.cataloComboBox.setItemText(0, _translate("Dialog", "All Catalogs", None))
        self.cataloComboBox.setItemText(1, _translate("Dialog", "ANF", None))
        self.cataloComboBox.setItemText(2, _translate("Dialog", "GCMT", None))
        self.cataloComboBox.setItemText(3, _translate("Dialog", "NEIC PDE", None))
        self.cataloComboBox.setItemText(4, _translate("Dialog", "ISC", None))
        self.typeComboBox.setItemText(0, _translate("Dialog", "All Types", None))
        self.typeComboBox.setItemText(1, _translate("Dialog", "MB", None))
        self.typeComboBox.setItemText(2, _translate("Dialog", "ML", None))
        self.typeComboBox.setItemText(3, _translate("Dialog", "MS", None))
        self.typeComboBox.setItemText(4, _translate("Dialog", "MW", None))
        self.locationGroupBox.setTitle(_translate("Dialog", "Location Box", None))
        self.centerLabel.setText(_translate("Dialog", "Location", None))
        self.closeButton.setText(_translate("Dialog", "Close Window", None))

