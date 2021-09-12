import admin as ad

i = ad.Admin("arthur", "muslimov")

print("I am admin. My rights:", end="\n\t")
i.privileges.show_privileges()
