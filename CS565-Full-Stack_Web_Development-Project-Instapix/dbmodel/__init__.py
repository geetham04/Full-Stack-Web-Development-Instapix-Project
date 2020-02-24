from .model_sqlite3 import model_sqlite3

appmodel = model_sqlite3()

def get_model():
    return appmodel
