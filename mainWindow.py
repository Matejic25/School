from PyQt6 import QtCore, QtGui, QtWidgets
from tableWindow import Ui_Table


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(857, 739)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(118, 118, 118)\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(247, 247, 247)\n"
"}")
        self.lineEdit.setMaxLength(3000)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.clicked.connect(self.btnClicked)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(247, 247, 247)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "PIB:"))
        self.pushButton.setText(_translate("MainWindow", "Pretraži"))

    def btnClicked(self):
        value = self.lineEdit.text()
        self.lineEdit.clear()
        self.ui = Ui_Table(value)
        self.ui.show_data()
        self.ui.table.show()
        return value


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
