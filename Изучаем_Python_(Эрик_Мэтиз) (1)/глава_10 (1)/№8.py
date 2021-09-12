
dogs_file = "txts\dogs.txt"
cats_file = "cats.txt"

try:
    with open(dogs_file) as f_dogs:
        dog_names = f_dogs.read()

    print("Dogs:")
    print(dog_names)
except FileNotFoundError:
    print("File " + dogs_file + " - not found.")
finally:
    print()

try:
    with open(cats_file) as f_cats:
        cat_names = f_cats.read()

    print("Cats:")
    print(cat_names)
except FileNotFoundError:
    print("File " + cats_file + " - not found.")
finally:
    print()
