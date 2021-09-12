
file_path = "txts\guest_book.txt"

with open(file_path, "a") as guest_book:
    while True:
        name = input("Please, enter your name: ")
        message = "Hello, " + name.title() + "!\n"
        
        print(message)
        guest_book.write(message)

    
