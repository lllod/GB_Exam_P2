# import model.add_notes
from model import add_notes, read_notes, delete_notes, editing_notes
# import delete_notes
# import editing_notes
# import read_notes
# import add_notes


class NotesModel:
    def __init__(self):
        self.add = add_notes.AddNote()
        self.read = read_notes.ReadNotes()
        self.delete = delete_notes.DeleteNote()
        self.editing = editing_notes.EditingNote()

    def add_note(self, user_text: str):
        self.add.add_note(user_text)

    def show_notes(self):
        self.read.show_all_notes()

    def show_notes_sortedby(self):
        self.read.show_all_notes_orderby()

    def show_notes_sortedby_desc(self):
        self.read.show_all_notes_orderby_desc()

    def delete_note(self, note_id: int):
        self.delete.delete_note(note_id)

    def editing_note(self, note_id: int, user_text: str):
        self.editing.editing_note(note_id, user_text)

    def show_one_note(self, note_id: int):
        self.read.show_one_note(note_id)




