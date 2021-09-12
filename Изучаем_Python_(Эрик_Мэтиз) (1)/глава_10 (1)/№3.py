
file_path = "txts\guest.txt"

with open(file_path, "w") as guest_file:
    name = input("Please, enter your name: ")

    guest_file.write(name + "\n")
