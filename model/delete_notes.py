from database.db import DataBase

database = DataBase()


class DeleteNote:
    def __init__(self, note_id: int):
        self.__note_id = note_id

    def add_note(self):
        database.delete_db_note(self.__note_id)
        print('Заметка успешно удалена!')
