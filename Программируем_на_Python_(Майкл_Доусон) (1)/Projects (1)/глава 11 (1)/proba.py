# проба графики

from livewires import games

games.init(screen_width = 960, screen_height = 650, fps = 120)
bund = games.load_image("D:\getimg.jpg", transparent = True) #False
games.screen.background = bund

games.screen.mainloop()
