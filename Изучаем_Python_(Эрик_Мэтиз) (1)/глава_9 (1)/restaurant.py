"""Класс для ресторанов"""

class Restaurant():
    """Простая модель ресторана"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.title = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит инфо о ресторане"""
        print("\"" + self.title.title() + "\" has " + 
              self.cuisine_type + " cuisine.")
    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт"""
        print("\"" + self.title.title() + "\" is open!")
