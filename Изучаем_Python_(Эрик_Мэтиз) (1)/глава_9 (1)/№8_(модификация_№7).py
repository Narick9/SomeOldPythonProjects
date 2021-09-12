class User():
    """Модель пользователя"""

    def __init__(self, first_name, last_name, **info):
        """Использует атрибуты описания пользователя"""
        self.gloss = {
            "first name": first_name.title(),
            "last name": last_name.title(),
            "full name": first_name.title() + " " + last_name.title()
            }

        for key, value in info.items():
            self.gloss[key] = value

    def describe_user(self):
        """Описывает пользователя"""
        print(self.gloss["full name"].title() + " info:")
        for key, value in self.gloss.items():
            print("\t" + key + ": " + str(value))
    def greet_user(self):
        """Персональное приветствие пользователя"""
        print("Hello, " + self.gloss["first name"] + "!")


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



i = Admin("Arthur", "Muslimov")

print("I am admin. My rights:", end = "\n\t")
i.privileges.show_privileges()
