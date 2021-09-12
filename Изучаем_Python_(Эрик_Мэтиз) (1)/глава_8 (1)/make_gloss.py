def make_car_gloss(mark, model, **other_infos):
    """Создает словарь по описанию автомобиля"""
    gloss = {}
    
    gloss["manufacturer"] = mark
    gloss["model"] = model
    
    for key, value in other_infos.items():
        gloss[key] = value

    return gloss
