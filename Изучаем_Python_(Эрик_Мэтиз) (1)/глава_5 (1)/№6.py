age = 16
print("Ваш возраст - " + str(age))

if age < 2:
    stage = "младенец"
elif age < 4:
    stage = "малыш"
elif age < 13:
    stage = "ребёнок"
elif age < 20:
    stage = "подросток"
elif age < 65:
    stage = "взрослый"
else:
    stage = "пожилой"

print("Вы " + stage)
