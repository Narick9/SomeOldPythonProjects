with open("txts\pi_digits.txt") as pi:
    text = pi.read()
    print(text)

print("\n----------------\n")

with open("txts\pi_million_digits.txt") as pi:
    pi_string = ""
    for line in pi:
        pi_string += line.strip()

    print("First 50 digits of pi:", end="\n\t")
    print(pi_string[:50], end="\n\n")

    number = input("Enter your phone number and find out if he is \n" +
                   "in first million of digits of pi: ")

    if number in pi_string:
        print("Yes, you are lucky!")
    else:
        print("Oh, you are out of luck.")

# print("----------------")
