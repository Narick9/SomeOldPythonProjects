users = ["admin", "Musya", "ya", "Arthur", "Angela"]

for user in users:
    if user.lower() == "admin":
        print("Привет, admin! Пришло новое сообщение об улучшении.")
    else:
        print("Привет, " + user + "! Вас давно не было.")
        
