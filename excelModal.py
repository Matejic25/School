from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setObjectName("Dialog")
        self.dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        self.dialog.resize(300, 200)
        self.dialog.setStyleSheet("QDialog{\n"
         "    background-color: rgb(190, 190, 190)\n"
         "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        # Line Edit
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                 "    background-color: rgb(236, 236, 236)\n"
                                 "}")
        self.verticalLayout.addWidget(self.lineEdit)

        # Button Box
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalLayoutWidget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi()
        self.buttonBox.accepted.connect(self.dialog.accept)
        self.buttonBox.rejected.connect(self.dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.dialog.setWindowTitle(_translate("Dialog", "U Excel"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Naziv fajla:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec())
