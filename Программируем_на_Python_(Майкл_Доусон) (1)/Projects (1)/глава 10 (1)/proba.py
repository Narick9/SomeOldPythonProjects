# проба gui

from tkinter import *
from random import *

class Application(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()
        self.widget()

    def widget(self):
        self.label = Label(self, text = "Это табличка. Ты её читаешь.")
        self.label.grid(row = 1, column = 0, columnspan = 2, sticky = E)
        self.button = Button(self)
        self.button["text"] = "Нажми меня"
        self.button["command"] = self.do
        self.button.grid(row = 2, column = 1, sticky = E)
        self.text = Text(self, width = 30, height = 10, wrap = WORD)
        self.text.grid(row = 3, column = 1)

    def do(self):
        self.button["text"] = chr(choice(range(256)))

root = Tk()
root.title("проба")
root.geometry("200x100")
app = Application(root)
root.mainloop()
