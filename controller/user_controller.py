from model.logic_models import UserModel

class UserController:
    def __init__(self, user_model=None):
        self.user_model = user_model if user_model else UserModel()

    def add_user(self, name, lastname):
        user = self.user_model.add_user(name, lastname)
        if user:
            return True
        else:
            return False

    def get_all_users_for_display(self):
        users_data = self.user_model.get_all_users()
        return users_data