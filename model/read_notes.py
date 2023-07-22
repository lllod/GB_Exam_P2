from database.db import DataBase


class ReadNotes:
    def __init__(self):
        self.__database = DataBase()

    def show_all_notes(self) -> list:
        return self.__database.show_db_all_notes()

    def show_all_notes_orderby(self) -> list:
        return self.__database.show_db_all_notes_sorted()

    def show_all_notes_orderby_desc(self) -> list:
        return self.__database.show_db_all_notes_sorted_desc()

    def show_one_note(self, note_id: int) -> list:
        return self.__database.read_db_note(note_id)
