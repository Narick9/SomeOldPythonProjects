from user import Admin

i = Admin("arthur", "muslimov")

print("I am admin. My rights:", end="\n\t")
i.privileges.show_privileges()
