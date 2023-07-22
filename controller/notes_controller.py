from view import menu
from model.notes_model import NotesModel
from database.db import DataBase
import os


class NotesController:
    def __init__(self):
        self.__notes_model = NotesModel()
        self.__main_menu = menu.MainMenu()
        self.__database = DataBase()
        self.__user_choice = ''
        self.__user_choice_show_menu = ''

    def __menu_choose(self, user_choice: str):
        if os.path.exists(os.path.join(os.path.dirname(__file__), 'notes.sqlite')) is False:
            self.__database.create_db()
        match int(user_choice):
            case 1:
                add_title = input('<!-- Введите заголовок заметки: --!>\n')
                add_text = input('<!-- Введите текст заметки: --!>\n')
                self.__notes_model.add_note(add_title, add_text)
                print('<!-- Заметка успешно добавлена! --!>')
            case 2:
                self.__user_choice_show_menu = self.__main_menu.show_menu_print()
                if self.__try_show_menu(self.__user_choice_show_menu):
                    match int(self.__user_choice_show_menu):
                        case 1:
                            result = self.__notes_model.show_notes()
                            self.__print_result_list(result)
                        case 2:
                            result = self.__notes_model.show_notes_sortedby()
                            self.__print_result_list(result)
                        case 3:
                            result = self.__notes_model.show_notes_sortedby_desc()
                            self.__print_result_list(result)
                        case 4:
                            return self.main()
                else:
                    return self.main()
            case 3:
                try:
                    note_id = int(input('<!-- Введите номер заметки, которую Вы хотите найти: --!> '))
                    if not self.__note_exists(note_id):
                        return self.main()
                    result = self.__notes_model.show_one_note(note_id)
                    self.__print_result_list(result)
                except ValueError:
                    print('<!-- Вы ввели некорректный номер заметки! Попробуйте еще раз: --!>')
            case 4:
                try:
                    note_id = int(input('<!-- Введите номер заметки, которую Вы хотите изменить: --!> '))
                    if not self.__note_exists(note_id):
                        return self.main()
                    ed_title = input('<!-- Введите новый заголовок заметки: --!>\n')
                    ed_text = input('<!-- Введите новый текст заметки: --!>\n')
                    self.__notes_model.editing_note(note_id, ed_title, ed_text)
                    print('<!-- Заметка успешно отредактирована! --!>')
                except ValueError:
                    print('<!-- Вы ввели некорректный номер заметки! Попробуйте еще раз: --!>')
            case 5:
                try:
                    note_id = int(input('<!-- Введите номер заметки, которую Вы хотите удалить: --!> '))
                    if not self.__note_exists(note_id):
                        return self.main()
                    self.__notes_model.delete_note(note_id)
                    print('<!-- Заметка успешно удалена! --!>')
                except ValueError:
                    print('<!-- Вы ввели некорректный номер заметки! Попробуйте еще раз: --!>')
            case 6:
                print('\n<!-- Завершена работа со справочником --!>')
                return 0
        return self.main()

    def __note_exists(self, note_id: int):
        if note_id not in self.__database.get_id():
            print('<!-- Такой записи нет! Повторите запрос: --!>')

    @staticmethod
    def __print_result_list(result_list):
        if not result_list:
            print('<!-- Заметок нет! --!>')
        else:
            for i in range(len(result_list)):
                print(f'\n№ {result_list[i][0]} | Дата: {result_list[i][3]}\n'
                      f'Заголовок: {result_list[i][1]}\n{result_list[i][2]}')

    @staticmethod
    def __try_show_menu(user_choice_show_menu):
        try:
            int(user_choice_show_menu)
        except ValueError:
            print('<!-- Вы ввели некорректный номер меню! Попробуйте еще раз: --!>')
            return 0
        if int(user_choice_show_menu) > 4 or int(user_choice_show_menu) < 1:
            print('<!-- Вы ввели некорректный номер меню! Попробуйте еще раз: --!>')
            return 0
        return 1

    def main(self):
        self.__user_choice = self.__main_menu.menu_print()
        try:
            int(self.__user_choice)
        except ValueError:
            print('<!-- Вы ввели некорректный номер меню! Попробуйте еще раз: --!>')
            return self.main()
        if 1 <= int(self.__user_choice) <= 6:
            return self.__menu_choose(self.__user_choice)
        print('<!-- Вы ввели некорректный номер меню! Попробуйте еще раз: --!>')
        return self.main()
