import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setFixedSize(975, 679)
    sys.exit(app.exec())