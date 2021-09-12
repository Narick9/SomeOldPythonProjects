"""Класс для представления админа"""

from user import User

class Privileges():
    """Список привилегий"""

    def __init__(self):
        self.privileges = [
            "right to add new message",
            "right to delete message",
            "right to ban users",
            ]

    def show_privileges(self):
        """Выводит список privileges"""
        separator = ", "
        print(separator.join(self.privileges))

    
class Admin(User):
    """User с привилегиями"""

    def __init__(self, first_name, last_name, **info):
        super().__init__(first_name, last_name, **info)
        
        self.privileges = Privileges()
