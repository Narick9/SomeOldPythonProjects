sandwich_orders = ["bacon sandwich", "beef sandwich", "cheese sandwich"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("The " + sandwich.title() + " is ready.")
    finished_sandwiches.append(sandwich)

print("\nAll orders are ready!")

print("Orders' list:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())
