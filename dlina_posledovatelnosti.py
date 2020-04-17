alist = []
count = 0
while count == 0:
    num = int(input())
    if num != 0:
        alist.append(num)
    else:
        print(len(alist))
        count += 1
