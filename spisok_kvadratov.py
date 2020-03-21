def natural(num):
    rang = range(n)
    num = 0
    nat = [0]
    while num == n:
        nums = rang[num]
        if nums % 2 == 0:
            num += 1 
        elif nums % 3 == 0:
            num += 1
        elif nums % 5 == 0:
            num += 1
        elif nums % 7 == 0:
            num += 1
        elif nums % 9 == 0:
            num += 1
        elif nums % 11 == 0:
            num += 1
        elif nums % 13 == 0:
            num += 1
        elif nums % 17 == 0:
            num += 1
        elif nums % 23 == 0:
            num += 1
        else:
            nat = nat.append(nums)
    return rang

nat = 0
n = int(input())
func = natural(n)
print(func)
