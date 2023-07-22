from model import add_note, read_notes, delete_note, editing_note


class NotesModel:
    def __init__(self):
        self.__add = add_note.AddNote()
        self.__read = read_notes.ReadNotes()
        self.__delete = delete_note.DeleteNote()
        self.__editing = editing_note.EditingNote()

    def add_note(self, title: str, text: str) -> None:
        return self.__add.add_note(title, text)

    def show_notes(self) -> list:
        return self.__read.show_all_notes()

    def show_notes_sortedby(self) -> list:
        return self.__read.show_all_notes_orderby()

    def show_notes_sortedby_desc(self) -> list:
        return self.__read.show_all_notes_orderby_desc()

    def show_one_note(self, note_id: int) -> list:
        return self.__read.show_one_note(note_id)

    def delete_note(self, note_id: int) -> None:
        return self.__delete.delete_note(note_id)

    def editing_note(self, note_id: int, title: str, text: str) -> None:
        return self.__editing.editing_note(note_id, title, text)




