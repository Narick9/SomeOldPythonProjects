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


class IceCreamStand(Restaurant):
    """Модель киоска с мороженым"""
    def __init__(self, restaurant_name, cuisine_type):
        """Наследует атрибуты из Restaurant и добаляет список сортов"""
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ["strawberry", "chocolate", "classic"]

    def describe_flavors(self):
        separator = ", "
        print(separator.join(self.flavors))


my_kiosk = IceCreamStand("Ice", "normal")
my_kiosk.describe_flavors()
