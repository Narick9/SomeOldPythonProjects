favorite_nums = {
    "Arthur": [9],
    "Musya": [666, 999],
    "Tosya": [100500, 0],
    "Ryzhik": [12, 24],
    "mcLamp": [2, 3],
    }

for name, nums in favorite_nums.items():
    print(name + ":", end = " ")
    for num in nums:
        print(str(num), end = ", ")
    print()
