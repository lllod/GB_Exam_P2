from database.db import DataBase


class AddNote:
    # def __init__(self, new_note: str):
    #     self.__new_note = new_note

    def add_note(self, user_text: str):
        database = DataBase()
        database.create_db()
        database.add_db_note(user_text)
        print('Заметка успешно добавлена!')
