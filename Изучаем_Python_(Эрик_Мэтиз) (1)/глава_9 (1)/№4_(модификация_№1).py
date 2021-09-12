class Restaurant():
    """Простая модель ресторана"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.title = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит инфо о ресторане"""
        print("\"" + self.title.title() + "\" has " + 
              self.cuisine_type + " cuisine.")
    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт"""
        print("\"" + self.title.title() + "\" is open!")
    def set_number_served(self, set_number):
        """Задаёт число обслуженных посетителей"""
        self.number_served = set_number
    def increment_number_served(self, increment):
        """
        Прибовляет к числу обслуженных  посетителей
        заданное число новых
        """
        self.number_served += increment
        

restaurant = Restaurant("arthur", "normal")

print("My restaurant title is \"" + restaurant.title.title() + "\".")
print("My restaurant's cuisine type is " + restaurant.cuisine_type + ".")
print()

restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
print("Restaurant served " + str(restaurant.number_served) + " people.")

restaurant.number_served = 9
print("Restaurant served " + str(restaurant.number_served) + " people.")

restaurant.set_number_served(45)
print("Restaurant served " + str(restaurant.number_served) + " people.")

restaurant.increment_number_served(68)
print("Restaurant served " + str(restaurant.number_served) + " people.")
