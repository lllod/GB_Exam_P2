from database.db import DataBase

database = DataBase()


class AddNote:
    def __init__(self, new_note: str):
        self.__new_note = new_note

    def add_note(self):
        database.add_db_note(self.__new_note)
        print('Заметка успешно добавлена!')
