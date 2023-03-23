import sys
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setFixedSize(900, 622)
    sys.exit(app.exec())
