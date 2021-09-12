# Trivia Challenge
# Trivia game that reads a plain text file
# Модифицирована по условию задачи главы 7

import sys

# Модифицированная функция
def open_file(file_name, mode, encoding_rus = False):
    """Open a file."""
    try:
        if encoding_rus:
            the_file = open(file_name, mode, encoding = "utf-8")
        else:
            the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

# Модифицированная функция
def next_line(the_file, not_new_line = False):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    if not_new_line:
        line = line.replace("\n", "")
    return line

# модифицированная функция
def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    
    if correct:
        correct = correct[0]

    # добавлена часть
    # считывает количество очков за вопрос
    question_score = next_line(the_file)
    if question_score:
        question_score = int(question_score[0])
                
    explanation = next_line(the_file) 

    return category, question, answers, correct, question_score, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

# Добавленная функция
def record_table(the_file):
    """Выводит отсортированный список рекордов"""
    print("Таблица рекордов: ")
    record_list = []

    name = next_line(the_file, not_new_line = True)
    score = next_line(the_file, not_new_line = True)
    if not name:
        print("Нет данных")
        return
    while name:
        record_list.append([score, name])
        name = next_line(the_file, not_new_line = True)
        score = next_line(the_file, not_new_line = True)
    record_list.sort(reverse = True)

    for i in range(len(record_list)):
        print(record_list[i][1], "\t", record_list[i][0])

# Модифицированная функция      
def main():
    record_file_write = open_file("record №4.txt", "a")
    trivia_file = open_file("эпизод.txt", "r", encoding_rus = True)
    
    title = next_line(trivia_file)
    welcome(title)

    record_file_read = open_file("record №4.txt", "r")
    record_table(record_file_read)
    record_file_read.close()
    
    score = 0
    print("\n")
    
    # get first block
    category, question, answers, correct, question_score, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += question_score
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, question_score, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)
    
    score = str(score)
    name = ""
    while not name:
        name = input("Введите ваше имя для таблицы рекордов: ")
    for line in (name, score):
        record_file_write.write(line + "\n")

    record_file_write.close()
 
main()  
input("\n\nPress the enter key to exit.")
