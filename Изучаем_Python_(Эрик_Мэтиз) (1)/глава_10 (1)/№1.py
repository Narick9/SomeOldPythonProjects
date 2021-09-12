
file_path = "txts\learning_python.txt"

with open(file_path) as facts_file:
    text = facts_file.read()
    print(text)
    print("---------")

with open(file_path) as facts_file:
    for line in facts_file:
        print(line.rstrip())
    print("---------")

with open(file_path) as facts_file:
    lines = facts_file.readlines()

for line in lines:
    print(line.rstrip())
