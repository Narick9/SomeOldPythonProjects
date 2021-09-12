
import json

file_path = "storage/favorite_num.json"

try:
    with open(file_path, "r") as f_obj:
        favorite_num = json.load(f_obj)
        
        print("And I know your favorite number! It is " +
              str(favorite_num) + ".")
except FileNotFoundError:
    print("I haven't memorized you number yet.")
