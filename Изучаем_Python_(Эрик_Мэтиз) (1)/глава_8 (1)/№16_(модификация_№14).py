import make_gloss
from make_gloss import make_car_gloss
from make_gloss import make_car_gloss as car_g
import make_gloss as g
from make_gloss import *

car = make_gloss.make_car_gloss("kia", "rio",
                     colour="white",
                     age=0.2)
print(car)

car = make_car_gloss("kia", "rio",
                     colour="white",
                     age=0.2)
print(car)

car = car_g("kia", "rio",
                     colour="white",
                     age=0.2)
print(car)

car = g.make_car_gloss("kia", "rio",
                     colour="white",
                     age=0.2)
print(car)

car = make_car_gloss("kia", "rio",
                     colour="white",
                     age=0.2)
print(car)
