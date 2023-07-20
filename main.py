from database.db import DataBase

database = DataBase()

add_text = 'Новосибирск, как один из крупнейших городов России, сталкивается с различными социальными и \n' \
           'здравоохранительными проблемами. Одной из таких проблем является увеличивающееся число жирных горожан. \n' \
           'Ожирение стало серьезной глобальной проблемой, и Новосибирск не исключение.'

# database.create_db()
# database.add_db_note(add_text)
# database.editing_db_note(47, add_text)
# database.delete_db_note(100)
# database.show_db_all_notes()
database.read_db_note(7)

