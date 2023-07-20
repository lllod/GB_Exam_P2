from controller import notes_controller


class MainMenu:
    def menu_print(self):
        data = {1: 'Добавить заметку',
                2: 'Показать все заметки',
                3: 'Поиск по номеру заметки',
                4: 'Редактировать заметку',
                5: 'Удалить заметку',
                6: 'Закончить работу'}
        print('-' * 10)
        print('\n'.join(f'{k}: {v}' for k, v in data.items()))
        print('-' * 10)
        if not user_choice():
            return 0
        menu_print()


    def user_choice(self):
        print('<!-- Что делаем? --!>')
        choice = int(input())
        if choice == 1:
            add_contact(file_name)
        elif choice == 2:
            searching_contact(file_name)
        elif choice == 3:
            update_contact(file_name)
        elif choice == 4:
            delete_contact(file_name)
        else:
            print('\n<!-- Завершена работа со справочником --!>')
            return 0
        return 1