people = [
    {"first_name": "arthur",
    "last_name": "muslimov",
    "age": 16,
    "city": "zelenodolsk",},
    
    {"first_name": "alan",
    "last_name": "turing",
    "age": 107,
    "city": "london",},
    
    {"first_name": "kun",
    "last_name": "cu",
    "age": 2570,
    "city": "chinatown"},
    ]



for human in people:
    for key, value in human.items():
        if key == "first_name":
            print(value.title() + ":")
        else:
            print("\t" + key.title() + ": " + str(value).title())
