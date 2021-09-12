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

restaurant = Restaurant("arthur", "normal")

print("My restaurant title is \"" + restaurant.title.title() + "\".")
print("My restaurant's cuisine type is " + restaurant.cuisine_type + ".")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()
