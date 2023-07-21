import sqlite3
from datetime import date


class DataBase:
    @staticmethod
    def create_db():
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_cursor = db_connect.cursor()
            db_cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            create_date TEXT NOT NULL,
            note_text TEXT NOT NULL)''')

    @staticmethod
    def add_db_note(text: str):
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_cursor = db_connect.cursor()
            current_date = str(date.today())
            db_cursor.execute('INSERT INTO notes (note_text, create_date) VALUES (?, ?)', (text, current_date))

    @staticmethod
    def editing_db_note(note_id: int, text: str):
        data = (text, note_id)
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_cursor = db_connect.cursor()
            db_cursor.execute('UPDATE notes SET note_text = ? WHERE id = ?', data)

    @staticmethod
    def delete_db_note(note_id: int):
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_cursor = db_connect.cursor()
            db_cursor.execute('DELETE FROM notes WHERE id = ?', (note_id, ))

    @staticmethod
    def show_db_all_notes():
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_connect.row_factory = sqlite3.Row
            db_cursor = db_connect.cursor()
            db_cursor.execute('SELECT id, note_text, create_date FROM notes')
            for result in db_cursor:
                print(result['id'], result['note_text'], result['create_date'])

    @staticmethod
    def show_db_all_notes_sorted():
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_connect.row_factory = sqlite3.Row
            db_cursor = db_connect.cursor()
            db_cursor.execute('SELECT id, note_text, create_date FROM notes ORDER BY create_date')
            for result in db_cursor:
                print(result['id'], result['note_text'], result['create_date'])

    @staticmethod
    def show_db_all_notes_sorted_desc():
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_connect.row_factory = sqlite3.Row
            db_cursor = db_connect.cursor()
            db_cursor.execute('SELECT id, note_text, create_date FROM notes ORDER BY create_date DESC')
            for result in db_cursor:
                print(result['id'], result['note_text'], result['create_date'])

    @staticmethod
    def read_db_note(note_id: int):
        with sqlite3.connect('notes.sqlite') as db_connect:
            db_connect.row_factory = sqlite3.Row
            db_cursor = db_connect.cursor()
            db_cursor.execute('SELECT id, note_text, create_date FROM notes WHERE id = ?', (note_id, ))
            for result in db_cursor:
                print(result['id'], result['note_text'], result['create_date'])
