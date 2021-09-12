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


users = [
    User("Arthur", "Muslimov", pets=["Musya", "Tosya"], age=16),
    User("Musya", "Muslimova", master="Arthur", age=92323),
    User("Tosya", "Muslimova", master="Arthur", colour="white"),
    ]

for user in users:
    user.greet_user()
    user.describe_user()
    print()
