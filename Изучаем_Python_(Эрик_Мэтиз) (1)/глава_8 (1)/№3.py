def make_shirt(size, text):
    """Создаёт новую футболку и описывает её"""
    print("Создана новая футболка размера "  + size +
          " с надписью \"" + text + "\".")

make_shirt("L", "T")
print()

make_shirt(size="XL", text="Text")
