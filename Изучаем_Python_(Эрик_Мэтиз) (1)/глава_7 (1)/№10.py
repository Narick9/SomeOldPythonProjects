holiday_responses = {}

print("--- Vacations poll ---")

active = ""
while active.lower() != "no":
    name = input("\nYour name: ")
    response = input("Where would you like to spend your vacation? ")

    holiday_responses[name] = response

    active = input("Are there anyone else who want to answer? (yes/no) ")

print("\nVacations polls results:")
for name, place in holiday_responses.items():
    print("\t" + name.title() + " - " + place)
