favorite_fruits = ("яблоко", "груша", "ананас")

fruits = ("банан", "апельсин", "мандарин", "яблоко", "ананас")
for fruit in fruits:
    if fruit.lower() in favorite_fruits:
        print("Ты действительно любишь " + fruit + "!")
