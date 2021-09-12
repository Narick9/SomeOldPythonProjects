# задача из главы 4

print("Задайте начало и конец счёта, а также интервал.")

start = int(input("Начало: "))
end = int(input("Конец: "))
ent = int(input("Интервал: "))

for let in range(start, end, ent):
    print(let)

input("\nДля выхода нажмите Enter.")
