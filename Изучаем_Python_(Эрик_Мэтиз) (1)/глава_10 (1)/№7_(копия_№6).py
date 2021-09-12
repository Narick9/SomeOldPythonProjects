
print("Enter 2 numbers and program will display their ammount.\n")

while True:
    f_num = input("First number: ")
    if f_num == "q":
        break

    s_num = input("Second number: ")
    if s_num == "q":
        break

    try:
        f_num = int(f_num)
        s_num = int(s_num)
    except ValueError:
        print("Enter only numbers!")
    else:
        print(f_num + s_num, end="\n")

    print()
        
    
    
