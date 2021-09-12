
file_path = ("txts/learning_python.txt")

with open(file_path) as facts_file:
    for line in facts_file:
        line = line.strip()
        print(line.replace("Python", "C"))
