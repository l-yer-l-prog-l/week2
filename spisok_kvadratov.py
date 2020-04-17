num = int(input())
spisok = []
count = 1
i = 0
while i < num:
    i = count ** 2
    count += 1
    if i <= num:
        print(i, end=" ")
