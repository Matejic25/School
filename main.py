from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

from mainWindow import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec())
