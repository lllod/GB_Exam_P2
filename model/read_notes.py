from database.db import DataBase

database = DataBase()


class ReadNotes:
    # def __init__(self, note_id=0):
    #     self.__note_id = note_id

    def show_all_notes(self):
        database.show_db_all_notes()

    def show_all_notes_orderby(self):
        database.show_db_all_notes_sorted()

    def show_all_notes_orderby_desc(self):
        database.show_db_all_notes_sorted_desc()

    def show_one_note(self, note_id: int):
        database.read_db_note(note_id)
