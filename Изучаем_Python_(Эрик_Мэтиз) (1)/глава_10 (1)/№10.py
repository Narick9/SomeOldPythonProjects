
books = [
    "Elizabeth, Empress of Austria",
    "Rx",
    "The Mystery of Lost River Canyon",
    ]

word = "the"

for book in books:
    try:
        with open("txts\\" + book + ".txt", encoding="UTF-8") as f_book:
            text = f_book.read()
            print("In book \"" + book + "\" word \"" + word + "\" occurs " +
                  str(text.lower().count("the")) + " times.")
    except FileNotFoundError:
        print("File \"txts\\" + book + ".txt\" not found.")
