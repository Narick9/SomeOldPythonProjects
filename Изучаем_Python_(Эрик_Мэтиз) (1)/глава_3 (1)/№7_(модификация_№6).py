neighbours = ["NoName_1", "NoName_2", "NoName_3",
              "NoName_4", "NoName_5", "NoName_6"]

message_1 = "Кошка по имени "
message_2 = " приглашена на обед."

print(message_1 + neighbours[0] + message_2)
print(message_1 + neighbours[1] + message_2)
print(message_1 + neighbours[2] + message_2)
print(message_1 + neighbours[3] + message_2)
print(message_1 + neighbours[4] + message_2)
print(message_1 + neighbours[5] + message_2)
print()

new_neighbours = ["NoName_7", "NoName_8", "NoName_9"]
new_neighbours_message = " добавлена в список приглашённых."

neighbours.insert(0, new_neighbours[0])
neighbours.insert(4, new_neighbours[1])
neighbours.append(new_neighbours[2])

print(message_1 + new_neighbours[0] + new_neighbours_message)
print(message_1 + new_neighbours[1] + new_neighbours_message)
print(message_1 + new_neighbours[2] + new_neighbours_message)
print()

print(message_1 + neighbours[0] + message_2)
print(message_1 + neighbours[1] + message_2)
print(message_1 + neighbours[2] + message_2)
print(message_1 + neighbours[3] + message_2)
print(message_1 + neighbours[4] + message_2)
print(message_1 + neighbours[5] + message_2)
print(message_1 + neighbours[6] + message_2)
print(message_1 + neighbours[7] + message_2)
print(message_1 + neighbours[8] + message_2)
print()

while len(neighbours) > 2:
    print("К несчастию, " + neighbours.pop() + " удалён из списка приглашения.")

print()
print(message_1 + neighbours[0] + message_2)
print(message_1 + neighbours[1] + message_2)
print()

while neighbours:
    del neighbours[0]

print(neighbours)
print()
