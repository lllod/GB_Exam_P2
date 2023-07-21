from database.db import DataBase

database = DataBase()


class EditingNote:
    def editing_note(self, note_id: int, note_text: str):
        database.editing_db_note(note_id, note_text)
        print('Заметка успешно отредактирована!')
