from database.db import DataBase

database = DataBase()


class DeleteNote:
    def delete_note(self, note_id: int):
        database.delete_db_note(note_id)
        print('Заметка успешно удалена!')
