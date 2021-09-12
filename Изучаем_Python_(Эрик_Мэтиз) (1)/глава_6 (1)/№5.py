rivers = {
    "волка": "россия",
    "амазонка": "бразилия",
    "райн": "германия",
    }

for river, country in rivers.items():
    print("Река " + river.title() + " протекает в стране " +
          country.title() + ".")
