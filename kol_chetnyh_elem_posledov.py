count = 0
alist = []
while count == 0:
    num = int(input())
    if num != 0:
        if num % 2 == 0:
            alist.append(num)
    else:
        print(len(alist))
        count += 1
