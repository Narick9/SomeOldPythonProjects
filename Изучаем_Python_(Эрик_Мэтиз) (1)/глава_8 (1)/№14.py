def make_car_gloss(mark, model, **other_infos):
    """Создает словарь по описанию автомобиля"""
    gloss = {}
    
    gloss["manufacturer"] = mark
    gloss["model"] = model
    
    for key, value in other_infos.items():
        gloss[key] = value

    return gloss

car = make_car_gloss("kia", "rio",
                     colour="white",
                     age=0.2)

print(car)
