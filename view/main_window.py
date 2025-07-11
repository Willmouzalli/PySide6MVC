from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first QMainWindow")
        self.setGeometry(300, 300, 250, 150)

