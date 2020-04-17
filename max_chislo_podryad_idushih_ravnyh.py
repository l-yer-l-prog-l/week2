count = 0
i = 0
alist = []
prev = 0
while count == 0:
    num = int(input())
    if num == prev:
        alist.append(num)
    if num != 0:
        i += 1
    else:
        print(len(alist) + 1)
        count += 1
    prev = num
