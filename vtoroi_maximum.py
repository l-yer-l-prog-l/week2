count = 0
alist = []
while count == 0:
    num = int(input())
    if num != 0:
        alist.append(num)
    else:
        maximum = max(alist)
        alist.remove(maximum)
        print(max(alist))
        count += 1
