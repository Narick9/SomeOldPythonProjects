def describe_city(title, country = "Russia"):
    """Описывает город"""
    print(title.title() + " is in " + country.title() + ".")

describe_city("zelenodolsk")
describe_city("zurich", "switzerland")
describe_city("amsterdam", "netherlands")
