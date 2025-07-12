from PySide6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first QMainWindow")
        self.setGeometry(300, 300, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.name_label = QLabel("Name: ")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Name")
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)

        self.lastname_label = QLabel("Last Name: ")
        self.lastname_edit = QLineEdit()
        self.lastname_edit.setPlaceholderText("Lastname")
        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_edit)

        self.add_user_button = QPushButton("Add User")
        layout.addWidget(self.add_user_button)

        self.status_label = QLabel("Status...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)


    def display_status_message(self, message):
        self.status_label.setText(message)


