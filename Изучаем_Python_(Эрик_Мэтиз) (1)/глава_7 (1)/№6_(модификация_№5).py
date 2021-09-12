exit_word = "quit"

print("Enter '" + exit_word + "' to exit.\n")

active = True
while active:
    enter = input("How old are you? ")

    if enter.lower() == exit_word:
        break
    
    age = int(enter)
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    if cost == 0:
        print("Movie ticket is free for you!")
    else:
        print("Movie ticket for you costs $" + str(cost) + ".")
    print()
