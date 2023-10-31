lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in lst:
    if num == 1 or num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
