# Игра "Отгодай число"
# Написана мной по псевдокоду
# Модифицирована по условию задачи №2 главы 10

from tkinter import *
from random import *

class Application(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        self.secret = randint(1, 100)
        self.try_n = 1
        self.widgets()

    def widgets(self):
        Label(self,
              text = "\t\"Отгодай число\""
              ).grid(row = 0, column = 0, columnspan = 4)
        Label(self,
              text = "Правила игры:"
              ).grid(row = 1, column = 0, sticky = W, columnspan = 4)
        Label(self,
              text = "\tПопробуйте отгодать число от 1 до 100"
              ).grid(row = 2, column = 0, sticky = W, columnspan = 4)
        Label(self,
              text = "\tс подсказками компьютера!"
              ).grid(row = 3, column = 0, sticky = W, columnspan = 4)
        self.try_n_lbl = Label(self,
                                text = "Попытка номер: " + str(self.try_n))
        self.try_n_lbl.grid(row = 4, column = 0, sticky = W)

        Label(self,
                text = "Ваш вариант:"
                ).grid(row = 5, column = 0, sticky = W)
        
        self.vvod = Entry(self)
        self.vvod.grid(row = 5, column = 2)

        self.btn = Button(self,
                          text = "Проверить",
                          command = self.logic)
        self.btn.grid(row = 6, column = 0, sticky = W)

        self.support_lbl = Label(self)
        self.support_lbl.grid(row = 7, column = 0, columnspan = 4, sticky = W)
        
        
    def logic(self):
        try:
            answer = int(self.vvod.get())
        except:
            self.support_lbl["text"] = "Это не число"
            print("except")
            return

        if answer == self.secret:
            self.support_lbl["text"] = "Ухты! Вы отгодали с " + str(self.try_n) + " попытки!"
            Button(self,
                   text = "Выход",
                   command = exit
                   ).grid(sticky = W)
        else:
            if self.secret < answer:
                self.support_lbl["text"] = "Число меньше"
            else:
                self.support_lbl["text"] = "Число больше"
            self.try_n += 1
            self.try_n_lbl["text"] = "Попытка номер: " + str(self.try_n)

def main():
    root = Tk()
    root.title("№2 отгодай число (модификация)")
    root.geometry("500x200")
    app = Application(root)
    root.mainloop()

try:
    main()
except:
    print("неизвестная ошибка")
    
    
