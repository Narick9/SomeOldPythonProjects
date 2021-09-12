neighbors = ["Муся", "Тося", "Рыжик", "NoName", "Маркис", "Кусьска", "Дуська"]

message_1 = "Кошка по имени "
message_2 = " приглашена на обед."

print(message_1 + neighbors[0] + message_2)
print(message_1 + neighbors[1] + message_2)
print(message_1 + neighbors[2] + message_2)
print(message_1 + neighbors[3] + message_2)
print(message_1 + neighbors[4] + message_2)
print(message_1 + neighbors[5] + message_2)
print(message_1 + neighbors[6] + message_2)

print()
print(neighbors[3] + " не сможет прийти.")
neighbors[3] = "NoName_1"
print()

print(message_1 + neighbors[0] + message_2)
print(message_1 + neighbors[1] + message_2)
print(message_1 + neighbors[2] + message_2)
print(message_1 + neighbors[3] + message_2)
print(message_1 + neighbors[4] + message_2)
print(message_1 + neighbors[5] + message_2)
print(message_1 + neighbors[6] + message_2)
