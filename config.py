import os
import sys

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS  # type: ignore # Suppress IDE warning for _MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))

BASE_APP_DIR = get_base_path()

user_home_dir = os.path.expanduser("~")

user_documents_dir = os.path.join(user_home_dir, "Documents")

APP_DATA_ROOT = os.path.join(user_documents_dir, "MVC_APP_DATA")

try:
    os.makedirs(APP_DATA_ROOT, exist_ok=True)
except OSError as e:
    print(f"ERROR: No se pudo acceder a APP_DATA_ROOT: {e}")

DATABASE_DIR = os.path.join(APP_DATA_ROOT, "data")

try:
    os.makedirs(DATABASE_DIR, exist_ok=True)
except OSError as e:
    print(f"ERROR: No se pudo acceder a DATABASE_DIR: {e}")

DATABASE_FILENAME = 'app_database.db'
DATABASE_PATH = os.path.join(DATABASE_DIR, DATABASE_FILENAME)

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
