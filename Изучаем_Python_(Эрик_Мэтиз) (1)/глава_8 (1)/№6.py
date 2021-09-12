def city_country(city, country):
    """Аккуратно форматирует город и страну"""
    return ", ".join([city.title(), country.title()])

print(city_country(city="zelenodolsk", country="russia"))
print(city_country(city="zurich", country="switzerland"))
print(city_country(city="amsterdam", country="netherlands"))
