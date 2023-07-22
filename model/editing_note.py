from database.db import DataBase


class EditingNote:
    def __init__(self):
        self.__database = DataBase()

    def editing_note(self, note_id: int, note_title: str, note_text: str):
        self.__database.editing_db_note(note_id, note_title, note_text)
