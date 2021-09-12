
import random as rand
import time

class Field():
    def __init__(self, x, y):
        self.map_x = x
        self.map_y = y
        self.field = []
        self.fieldnew = []
        for x in range(self.map_x):
            line = []
            for y in range(self.map_y):
                line.append(' ')
            self.field.append(line)
        self.fieldnew = self.field[:]

    def FieldShow(self):
        for y in range(self.map_y):
            for x in range(self.map_x):
                print(self.field[x][y], end="")
            print()

    def FieldClear(self):
        for y in range(self.map_y):
            for x in range(self.map_x):
                self.field[x][y] = ' '

    def AddFrame(self, x, y):
        if (    x == 0 or x == self.map_x - 1
            or  y == 0 or y == self.map_y - 1):
            self.field[x][y] = '#'

    def AddCells(self, x, y, chance):
        if ( not (x == 0 or x == self.map_x - 1
                  or y == 0 or y == self.map_y - 1)):
            if (rand.randint(1, chance) == 1):
                self.field[x][y] = 'O'

    def Life(self, x, y):
        if (not (x == 0 or x == self.map_x - 1
                 or y == 0 or y == self.map_y - 1)):
            neighboures = 0
            for ly in (-1, 0, 1):
                for lx in (-1, 0, 1):
                    if lx == 0 and ly == 0:
                        continue
                    if self.field[x + lx][y + ly] == 'O':
                        neighboures += 1
            if neighboures == 3:
                self.fieldnew[x][y] = 'O'
            elif neighboures < 2 or neighboures > 3:
                self.fieldnew[x][y] = ' '
                
    def Update(self):
        self.field = self.fieldnew[:]
            
            

if __name__ == "__main__":
    mymap = Field(100, 25)

    for y in range(mymap.map_y):
        for x in range(mymap.map_x):
            mymap.AddFrame(x, y)
            mymap.AddCells(x, y, 10)
    mymap.FieldShow()
    time.sleep(1)
    while True:
        for y in range(mymap.map_y):
            for x in range(mymap.map_x):
                mymap.Life(x, y)
        mymap.Update()
        mymap.FieldShow()
        time.sleep(1)
                
    
    
