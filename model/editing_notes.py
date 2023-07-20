from database.db import DataBase

database = DataBase()


class EditingNote:
    def __init__(self, note_id: int, note_text: str):
        self.__note_id = note_id
        self.__note_text = note_text

    def editing_note(self):
        database.editing_db_note(self.__note_id, self.__note_text)
        print('Заметка успешно отредактирована!')
