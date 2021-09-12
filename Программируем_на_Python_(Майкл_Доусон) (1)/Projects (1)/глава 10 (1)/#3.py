# По условию задачи №3 главы 10

from tkinter import *

class Application(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        self.row = 0
        self.col = 0
        
        self.widgets()

    def get_row(self):
        row = self.row
        self.row += 1
        return row

    def widgets(self):
        Label(self,
              text = "Меню нашего ресторана"
              ).grid(row = self.get_row(), columnspan = 4)

        self.truffell = BooleanVar()
        self.meat = BooleanVar()
        self.wine = BooleanVar()
        self.chooses = [[self.truffell, "Утка под гарниром из трюфеля", 300],
                   [self.meat, "Мясной стейк из мраморной говядины", 100],
                   [self.wine, "Итальянское вино 1928 года", 800]]
        for part in self.chooses:
            row = self.get_row()
            Checkbutton(self,
                        text = part[1] + "\t\t",
                        variable = part[0]
                        ).grid(row = row, columnspan = 3,
                                sticky = W)
            Label(self,
                  text = str(part[2]) + "$"
                  ).grid(row = row, column = 4, sticky = W)

        Button(self,
               text = "Заказать",
               command = self.print_check
               ).grid(row = self.get_row(), sticky = W)

        self.cost_lbl = Label(self,
                        text = "Ваш заказ обойдётся вам в 0$")
        self.cost_lbl.grid(row = self.get_row(), sticky = W)

    def print_check(self):
        cost = 0
        for part in self.chooses:
            if part[0].get():
                cost += part[2]

        self.cost_lbl["text"] = "Ваш заказ обойдётся вам в " + str(cost) + "$"

        

def main():
    root = Tk()
    root.title("Счет, пожалуйста!")
    app = Application(root)
    root.mainloop()

main()
        
