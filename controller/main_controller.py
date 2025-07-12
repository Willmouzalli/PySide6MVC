from controller.user_controller import UserController
from model.logic_models import UserModel
from view.main_window import MainWindow
from model.database_manager import Engine, Base

class MainController:
    def __init__(self, main_window=None):
        self.main_window = None
        self.user_controller = None
        self.user_controller = UserModel()

    def initialize_database(self):
        print("Initializing database")
        try:
            Base.metadata.create_all(bind=Engine)
            print("Database initialized")
        except Exception as e:
            print(e)

    def show_main_window(self):
        self.initialize_database()
        self.main_window = MainWindow()
        self.user_controller = UserController(user_model=self.user_controller)
        add_user_button = self.main_window.add_user_button
        add_user_button.clicked.connect(self.on_add_user_button_clicked)
        self.main_window.show()
        print("Showing principal window")

    def on_add_user_button_clicked(self):
        user_name = self.main_window.name_edit.text()
        user_lastname = self.main_window.lastname_edit.text()

        if self.user_controller.add_user(user_name, user_lastname):
            self.main_window.name_edit.clear()
            self.main_window.lastname_edit.clear()
            self.main_window.display_status_message(f"Added {user_name} user.")
        else:
            self.main_window.display_status_message(f"Error adding user {user_name}.")
            print("User already exists")


