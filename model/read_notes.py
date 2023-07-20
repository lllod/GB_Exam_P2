from database.db import DataBase

database = DataBase()


class ReadNotes:
    def __init__(self, note_id: int):
        self.__note_id = note_id

    def show_all_notes(self):
        database.show_db_all_notes()

    def show_one_note(self):
        database.read_db_note(self.__note_id)
