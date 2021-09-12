alien_colour = "red"

print("Подбит корабль пришельцев!\n")

if alien_colour == "green":
    score = 5
elif alien_colour == "yellow":
    score = 10
else:
    score = 15

print("Вы получили " + str(score) + " очков")
