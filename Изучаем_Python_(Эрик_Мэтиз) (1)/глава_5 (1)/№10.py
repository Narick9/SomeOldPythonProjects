current_users = ["arthur", "gabriella", "tosya", "ryzhik", "kuzya"]
new_users = ["Tishka", "Mysyazavr", "KuZya", "Musya", "Gabriella"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Логин '" + new_user + "' недоступен. Выберите другой логин.")
    else:
        print("Логин '" + new_user + "' доступен")
