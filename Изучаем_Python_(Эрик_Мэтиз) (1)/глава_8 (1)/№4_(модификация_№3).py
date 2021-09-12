def make_shirt(size="L", text="I love Python."):
    """Создаёт новую футболку и описывает её"""
    print("Создана новая футболка размера "  + size +
          " с надписью \"" + text + "\".")

make_shirt("L")
print()

make_shirt(size="M", text="I don't know my size")
