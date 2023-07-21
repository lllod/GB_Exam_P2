from view import menu
from model.notes_model import NotesModel


class NotesController:
    def __init__(self):
        self.notes_model = NotesModel()
        self.main_menu = menu.MainMenu()

    def menu_choose(self, user_choice: int):
        match user_choice:
            case 1:
                add_text = input('Введите текст заметки:\n')
                self.notes_model.add_note(add_text)
            case 2:
                user_choice_show_menu = self.main_menu.show_menu_print()
                match user_choice_show_menu:
                    case 1:
                        self.notes_model.show_notes()
                    case 2:
                        self.notes_model.show_notes_sortedby()
                    case 3:
                        self.notes_model.show_notes_sortedby_desc()
                    case 4:
                        self.main()
            case 3:
                note_id = int(input('Введите номер заметки, которую Вы хотите найти: '))
                self.notes_model.show_one_note(note_id)
            case 4:
                note_id = int(input('Введите номер заметки, которую Вы хотите изменить: '))
                ed_text = input('Введите новый текст заметки:\n')
                self.notes_model.editing_note(note_id, ed_text)
            case 5:
                note_id = int(input('Введите номер заметки, которую Вы хотите удалить: '))
                self.notes_model.delete_note(note_id)
            case 0:
                return 0
        self.main()

    def main(self):
        user_choice = self.main_menu.menu_print()
        self.menu_choose(user_choice)
