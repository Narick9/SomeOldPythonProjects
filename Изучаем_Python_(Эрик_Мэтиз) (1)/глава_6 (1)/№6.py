favorite_laguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

not_voted = ["arthur", "musya", "tosya", "phil"]

for name in set(not_voted):
    name = name.title()
    if name in favorite_laguages.keys():
        print("Спасибо вам, что проголосовали в нашем опросе, " + name + "!")
    else:
        print("Не хотите ли вы принять участие в нашем опросе, " + name + "?")
