from view.main_window import MainWindow
from model.database_manager import Engine, Base

class MainController:
    def __init__(self):
        self.main_window = None

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
        self.main_window.show()
        print("Showing principal window")