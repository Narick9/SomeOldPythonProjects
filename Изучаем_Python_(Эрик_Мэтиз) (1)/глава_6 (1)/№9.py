favorite_places = {
    "артур": ["дом"],
    "муся": ["кормушка", "кровать", "мой стол"],
    "тося": ["кормушка", "не моя кровать", "мой стол"],
    }

for human, places in favorite_places.items():
    print(human.title() + ":")

    comma = ", "
    print("\tPlaces: " + comma.join(places))
    
