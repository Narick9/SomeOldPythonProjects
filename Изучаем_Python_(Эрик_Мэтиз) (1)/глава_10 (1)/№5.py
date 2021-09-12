
file_path = "txts\poll_result.txt"

with open(file_path, "a") as poll:
    while True:
        answer = input("Why do you like to programming? ")
        
        if answer == "quit":
            break
        
        print("Thanks for you answer! We write it in file.\n")
        poll.write(answer + "\n")
