pizzas = ["мамина пицца", "пицца тёти Фариды", "бабушкина пицца"]

for pizza in pizzas:
    print(pizza + " - одна из моих самых любимых пицц.")
print("\nДа, я действительно люблю пиццу!")

friend_pizzas = pizzas[:]
pizzas.append("открытый пирог")
friend_pizzas.append("пицца с рыбой")

print()
print("Мои любимые пиццы: ", end = "")
for pizza in pizzas[:-1]:
    print(pizza, end = ", ")
print(pizzas[-1] + ".")

print()
print("Любимые пиццы моего друга: ", end = "")
for pizza in friend_pizzas[:-1]:
    print(pizza, end = ", ")
print(friend_pizzas[-1] + ".")
