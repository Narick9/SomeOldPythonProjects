# По условию задачи №1 из главы 10

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.widgets()
        
    def widgets(self):
        Label(self,
              text = "Эта программа сочинит рассказ о вас."
            ).grid(row = 0, column = 0, columnspan = 3)
        
        Label(self,
              text = "Ваше имя"
              ).grid(row = 1, column = 0, sticky = S)
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 2, column = 0, sticky = N)
        
        Label(self,
              text = "Имя вашего питомца"
              ).grid(row = 3, column = 0, sticky = S)
        self.pet_name_ent = Entry(self)
        self.pet_name_ent.grid(row = 4, column = 0, sticky = N)

        Label(self,
              text = "Ваш питомец:"
              ).grid(row = 1, column = 2)
        
        self.is_dirty = BooleanVar(self)
        Checkbutton(self,
                    text = "Грязный",
                    variable = self.is_dirty,
                    command = self.new_text
                    ).grid(row = 2, column = 2, sticky = W)

        self.is_religious = BooleanVar(self)
        Checkbutton(self,
                    text = "Религиозный",
                    variable = self.is_religious,
                    command = self.new_text
                    ).grid(row = 3, column = 2, sticky = W)

        self.is_pig = BooleanVar(self)
        Checkbutton(self,
                    text = "Свинообразный",
                    variable = self.is_pig,
                    command = self.new_text
                    ).grid(row = 4, column = 2, sticky = W)

        Label(self,
              text = "Вид питомца:"
              ).grid(row = 1, column = 3)
        self.who_is_pet = StringVar(self)
        self.who_is_pet.set("Нечто")
        pets = ["Кошка", "Муся"]
        row_i = 2
        for pet in pets:
            Radiobutton(self,
                        text = pet,
                        variable = self.who_is_pet,
                        value = pet,
                        command = self.new_text
                        ).grid(row = row_i, column = 3, sticky = W)
            row_i += 1

        Label(self,
              text = "Ваш шедевр"
              ).grid(row = 5, columnspan = 5)
        self.txt = Text(self,
                        width = 80, height = 5,
                        wrap = WORD)
        self.txt.grid(row = 6, column = 0, columnspan = 5)
        self.txt.insert(0.0, "")

    def new_text(self):
        name = self.name_ent.get()
        pet_name = self.pet_name_ent.get()
        pet = self.who_is_pet.get()
        abjectives = ""

        if self.is_dirty.get():
            abjectives += ", гразным"
        if self.is_religious.get():
            abjectives += ", религиозным"
        if self.is_pig.get():
            abjectives += ", свинообразным"

        if not (name and pet_name and pet):
            return
        
        rep = ""
        rep += "Отважный " + name + " со своим верным другом "
        rep += pet + " по имени "
        rep += pet_name + ", который, по своей сути, был умным" + abjectives
        rep += " животным, бороздили океан в поисках приключений."

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, rep)

def main():
    root = Tk()
    root.title("Сумасшедший сказочник (№1)")
    app = Application(root)
    root.mainloop()

try:
    main()
except:
    print("Неизвестная ошибка")
