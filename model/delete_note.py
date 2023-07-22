from database.db import DataBase


class DeleteNote:
    def __init__(self):
        self.__database = DataBase()

    def delete_note(self, note_id: int):
        self.__database.delete_db_note(note_id)
