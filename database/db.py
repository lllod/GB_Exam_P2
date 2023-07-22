import sqlite3
from datetime import date


class DataBase:
    def __init__(self):
        self.__db_cursor = None
        self.__current_date = str(date.today())

    def create_db(self) -> None:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_title TEXT NOT NULL,
            note_text TEXT NOT NULL,
            date TEXT NOT NULL)''')

    def add_db_note(self, title: str, text: str) -> None:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('INSERT INTO notes (note_title, note_text, date) VALUES (?, ?, ?)',
                                   (title, text, self.__current_date))

    def editing_db_note(self, note_id: int, title: str, text: str) -> None:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('UPDATE notes SET note_title = ?, note_text = ?, date = ? '
                                   'WHERE id = ?', (title, text, self.__current_date, note_id))

    def delete_db_note(self, note_id: int) -> None:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))

    def show_db_all_notes(self) -> list:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.db_connect.row_factory = sqlite3.Row
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('SELECT id, note_title, note_text, date FROM notes')
            return [[result['id'], result['note_title'], result['note_text'], result['date']] for result in
                    self.__db_cursor]

    def show_db_all_notes_sorted(self) -> list:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.db_connect.row_factory = sqlite3.Row
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('SELECT id, note_title, note_text, date FROM notes ORDER BY date')
            return [[result['id'], result['note_title'], result['note_text'], result['date']] for result in
                    self.__db_cursor]

    def show_db_all_notes_sorted_desc(self) -> list:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.db_connect.row_factory = sqlite3.Row
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('SELECT id, note_title, note_text, date FROM notes ORDER BY date DESC')
            return [[result['id'], result['note_title'], result['note_text'], result['date']] for result in
                    self.__db_cursor]

    def read_db_note(self, note_id: int) -> list:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.db_connect.row_factory = sqlite3.Row
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('SELECT id, note_title, note_text, date FROM notes WHERE id = ?', (note_id,))
            return [[result['id'], result['note_title'], result['note_text'], result['date']] for result in
                    self.__db_cursor]

    def get_id(self) -> list:
        with sqlite3.connect('notes.sqlite') as self.db_connect:
            self.db_connect.row_factory = sqlite3.Row
            self.__db_cursor = self.db_connect.cursor()
            self.__db_cursor.execute('SELECT id FROM notes')
            return [result['id'] for result in self.__db_cursor]
