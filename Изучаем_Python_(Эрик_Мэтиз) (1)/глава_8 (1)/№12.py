def make_sandwich(*toppings):
    """Создаёт сендвич с заданными начинками"""
    topping = ", ".join(toppings)
    print("Sandiwch with " + topping + " ready.")

make_sandwich("cheese", "sausage", "salad")
make_sandwich("cheese", "sausage")
make_sandwich("suasage", "bread")
