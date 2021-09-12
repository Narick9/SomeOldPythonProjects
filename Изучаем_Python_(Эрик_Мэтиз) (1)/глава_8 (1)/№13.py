def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("alber", "einstein",
                             location="princeton",
                             field="physics")
my_profile = build_profile("arthur", "muslimov",
                           location="zelenodolsk",
                           pet=["musya", "tosya"])

print(user_profile)
print(my_profile)
