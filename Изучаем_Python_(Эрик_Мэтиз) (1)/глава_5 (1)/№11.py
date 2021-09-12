nums = [i for i in range(1, 10)]

for num in nums:
    if num == 1:
        suff = "st"
    elif num == 2:
        suff = "nd"
    elif num == 3:
        suff = "rd"
    else:
        suff = "th"

    print(str(num) + suff)
    
