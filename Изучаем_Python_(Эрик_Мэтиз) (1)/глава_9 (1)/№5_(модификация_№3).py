class User():
    """Модель пользователя"""

    def __init__(self, first_name, last_name, **info):
        """Использует атрибуты описания пользователя"""
        self.f_name = first_name
        self.l_name = last_name

        self.login_attempts = 0
        
        self.gloss = {
            "first_name": first_name.title(),
            "last_name": last_name.title(),
            "full_name": first_name.title() + " " + last_name.title(),
            "login_atteps": self.login_attempts,
            }

        for key, value in info.items():
            self.gloss[key] = value

    def describe_user(self):
        """Описывает пользователя"""
        print(self.gloss["full_name"].title() + " info:")
        for key, value in self.gloss.items():
            print("\t" + key + ": " + str(value))
    def greet_user(self):
        """Персональное приветствие пользователя"""
        print("Hello, " + self.gloss["first_name"] + "!")
    def increment_login_attempts(self):
        """Увеличивает login_attempts на 1"""
        self.login_attempts += 1
        self.gloss["login_attempts"] = self.login_attempts
    def reset_login_attempts(self):
        """Обнуляет значение login_attempts"""
        self.login_attempts = 0
        self.gloss["login_attempts"] = self.login_attempts
        

users = [
    User("Arthur", "Muslimov", pets=["Musya", "Tosya"], age=16),
    User("Musya", "Muslimova", master="Arthur", age=92323),
    User("Tosya", "Muslimova", master="Arthur", colour="white"),
    ]

for user in users:
    user.greet_user()
    user.describe_user()
    print()


user = users[0]

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(user.gloss["full_name"] + ":")
print("\tlogin_attempts: " + str(user.gloss["login_attempts"]))

user.reset_login_attempts()

print(user.gloss["full_name"] + ":")
print("\tlogin_attempts: " + str(user.gloss["login_attempts"]))
