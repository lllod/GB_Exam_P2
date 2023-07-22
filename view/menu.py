class MainMenu:
    def __init__(self):
        self.__data = {}

    def menu_print(self) -> str:
        self.__data = {1: 'Добавить заметку',
                       2: 'Показать все заметки',
                       3: 'Поиск по номеру заметки',
                       4: 'Редактировать заметку',
                       5: 'Удалить заметку',
                       6: 'Закончить работу'}
        self.print_menu_elements(self.__data)
        return input()

    def show_menu_print(self) -> str:
        self.__data = {1: 'Показать заметки без сортировки',
                       2: 'Сначала старые записи',
                       3: 'Сначала новые записи',
                       4: 'Назад'}
        self.print_menu_elements(self.__data)
        return input()

    @staticmethod
    def print_menu_elements(data: dict):
        print('-' * 10)
        print('\n'.join(f'{k}: {v}' for k, v in data.items()))
        print('-' * 10)
        print('<!-- Выберите пункт меню --!>')
