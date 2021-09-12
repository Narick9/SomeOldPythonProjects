# мой логин и пароль

print("\tДобро пожаловать в мою личную сеть!\n")

login = ""
password = ""
security = 0

while not login:
    login = input("Логин: ")
while not password:
    password = input("Пароль: ")

if login == "Artur" and password == "Muslimov":
    print("Добро пожаловать, Артур!")
    security = 5
elif login == "Рыжик" and password == "Муслимов":
    print("Давно не виделись. Ты стал легендой.")
    security = 5
elif login == "Musya" and password == "Muslimova":
    print("Корм уже в кормушке!")
    security = 3
elif login == "Tosya" and password == "Muslimova":
    print("Новая игрушка уже куплена!")
    security = 3
elif login == "Guest" or password == "Guest":
    print("Добро пожаловать к нам в гости!")
    security = 1
else:
    print("Похоже, что вы не такой уж и экслюзивный пользователь.")

input("\n\nНажмите Enter для выхода.")
