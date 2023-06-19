from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QWidget, QComboBox
from excelModal import Ui_Dialog
from database import Database
import pandas as pd
import os


class Ui_Table(object):
    def __init__(self, pib):
        self.db = Database()
        self.company_id = self.db.get_company_id_by_pib(pib)
        self.table = QWidget()
        self.table.setObjectName("Table")
        self.table.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        self.table.setFixedSize(1220, 747)
        self.table.setStyleSheet("QWidget{\n"
                                 "    background-color: rgb(190, 190, 190)\n"
                                 "}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.table)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1200, 70))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 100, 80))
        self.verticalLayoutWidget.setMaximumSize(QtCore.QSize(200, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # Combo Box
        self.comboBox = QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(200, 30))
        #SR 101235431
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(50)
        self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setPlaceholderText("Adresa objekta")
        self.add_combo_box_items(pib)
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "    background-color: rgb(236, 236, 236)\n"
                                    "}")
        self.verticalLayout.addWidget(self.comboBox)
        self.addressSelect = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.addressSelect.clicked.connect(self.get_combo_box_item)
        self.addressSelect.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addressSelect.setFont(font)
        self.addressSelect.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(236, 236, 236)\n"
                                      "}")
        self.addressSelect.setObjectName("addressSelect")
        self.verticalLayout.addWidget(self.addressSelect)
        self.horizontalLayout.addWidget(self.verticalLayoutWidget)
        # Label 1
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 400, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "    background-color: rgb(236, 236, 236)\n"
                                 "}")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 70))
        self.label_2.setMaximumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    background-color: rgb(236, 236, 236)\n"
                                   "}")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget2 = QtWidgets.QWidget(parent=self.table)
        self.verticalLayoutWidget2.setMaximumSize(QtCore.QSize(200, 100))
        self.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget2)
        self.pushButton.clicked.connect(self.show_only_periodic)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color: rgb(236, 236, 236)\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget2)
        self.pushButton_2.clicked.connect(self.show_only_controlled)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(236, 236, 236)\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout2.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.verticalLayoutWidget2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.table)
        self.pushButton_3.clicked.connect(self.exportToExcel)
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(236, 236, 236)\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.table)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 1200, 621))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.horizontalLayoutWidget_2)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("QWidget{\n"
                                       "    background-color: rgb(236, 236, 236)\n"
                                       "}")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(208)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(38)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(pib)
        QtCore.QMetaObject.connectSlotsByName(self.table)


    def show_data(self):
        extinguishers = self.db.get_extinguishers_of_company_by_id(self.company_id)

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(extinguishers):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    ispravnost = row_data[3]
                    if ispravnost == 1:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("DA"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("NE"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def show_only_controlled(self):
        extinguishers = self.db.get_controlled_extinguishers_of_company_by_id(self.company_id)

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(extinguishers):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    ispravnost = row_data[3]
                    if ispravnost == 1:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("DA"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("NE"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def show_only_periodic(self):
        extinguishers = self.db.get_periodic_extinguishers_of_company_by_id(self.company_id)

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(extinguishers):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 3:
                    ispravnost = row_data[3]
                    if ispravnost == 1:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("DA"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("NE"))
                else:
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def exportToExcel(self):
        self.excelModal = Ui_Dialog()
        self.excelModal.dialog.show()
        if self.excelModal.dialog.exec():
            output_path = os.path.abspath(os.getcwd()).replace("\\", "/")
            file_name = self.excelModal.lineEdit.text()
            if len(file_name) > 0:
                columnHeaders = []
                for j in range(self.tableWidget.model().columnCount()):
                    columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

                df = pd.DataFrame(columns=columnHeaders)

                for row in range(self.tableWidget.rowCount()):
                    for col in range(self.tableWidget.columnCount()):
                        df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()
                df.to_excel(f'{output_path}/excel_tables/{file_name}.xlsx', index=False)
                print('Excel file exported')
            else:
                print('File name error')
        else:
            pass

    def retranslateUi(self, pib):
        company_name = self.db.get_company_name_by_id(self.db.get_company_id_by_pib(pib))
        _translate = QtCore.QCoreApplication.translate
        self.table.setWindowTitle(_translate("Table", "Table"))
        self.label.setText(_translate("Table", company_name))
        self.label_2.setText(_translate("Table", pib))
        self.addressSelect.setText(_translate("Table", "Izaberi"))
        self.pushButton.setText(_translate("Table", "Samo periodični"))
        self.pushButton_2.setText(_translate("Table", "Samo kontrolni"))
        self.pushButton_3.setText(_translate("Table", "U EXCEL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Table", "Tip"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Table", "Podaci o proizvođaču"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Table", "Fabrički broj"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Table", "Ispravnost"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def add_combo_box_items(self, pib):
        addresses = self.db.get_addresses_by_pib(pib)
        for address in addresses:
            self.comboBox.addItems(address)

    def get_combo_box_item(self):
        chosen = self.comboBox.itemText(self.comboBox.currentIndex())
        if chosen != '':
            extinguishers = self.db.get_extinguishers_of_company_at_certain_address(chosen, self.company_id)

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(extinguishers):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 3:
                        ispravnost = row_data[3]
                        if ispravnost == 1:
                            self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("DA"))
                        else:
                            self.tableWidget.setItem(row_number, column_number, QTableWidgetItem("NE"))
                    else:
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    # def get_extinguishers_on_address(self, chosen, pib):
