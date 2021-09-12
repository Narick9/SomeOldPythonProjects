
import json

file_path = "storage/favorite_num.json"

with open(file_path, "w") as f_obj:
    favorite_num = int(input("What is your favorite number? "))
    
    json.dump(favorite_num, f_obj)
    
    print("Well, I remember your favorite number. See you soon later.")
