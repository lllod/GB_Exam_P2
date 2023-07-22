from database.db import DataBase


class AddNote:
    def __init__(self):
        self.__database = DataBase()

    def add_note(self, title: str, text: str):
        self.__database.add_db_note(title, text)
