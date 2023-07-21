class MainMenu:
    def __init__(self):
        self.choice = 0
        self.data = {}

    def menu_print(self):
        self.data = {1: 'Добавить заметку',
                2: 'Показать все заметки',
                3: 'Поиск по номеру заметки',
                4: 'Редактировать заметку',
                5: 'Удалить заметку',
                6: 'Закончить работу'}
        print('-' * 10)
        print('\n'.join(f'{k}: {v}' for k, v in self.data.items()))
        print('-' * 10)
        # if not self.user_choice():
        #     return 0
        # self.menu_print()
        return self.user_choice()

    def show_menu_print(self):
        self.data = {1: 'Показать заметки без сортировки',
                2: 'Сначала старые записи',
                3: 'Сначала новые записи',
                4: 'Назад'}
        print('-' * 10)
        print('\n'.join(f'{k}: {v}' for k, v in self.data.items()))
        print('-' * 10)
        # if not self.user_choice():
        #     return 0
        return self.user_show_menu_choice()

    def user_show_menu_choice(self):
        print('<!-- Показать все заметки без сортировки или отсортировать по дате? --!>')
        self.choice = int(input())
        if self.choice == 1:
            return self.choice
        elif self.choice == 2:
            return self.choice
        elif self.choice == 3:
            return self.choice
        elif self.choice == 4:
            return self.choice
        else:
            self.show_menu_print()

    def user_choice(self):
        print('<!-- Что делаем? --!>')
        self.choice = int(input())
        if self.choice == 1:
            return self.choice
        elif self.choice == 2:
            return self.choice
        elif self.choice == 3:
            return self.choice
        elif self.choice == 4:
            return self.choice
        elif self.choice == 5:
            return self.choice
        else:
            print('\n<!-- Завершена работа со справочником --!>')
            return 0
