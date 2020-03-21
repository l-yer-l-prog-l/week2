N = str(input())
N.append(0)
last = int(N[1])
if ("0", "5", "6", "7", "8", "9" in last):
    print(N, 'korov')
elif last == 1 or int(N) == 1:
    print(N, 'korova')
else:
    print(N, 'korovy')
