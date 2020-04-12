N = int(input())
M = str(N)
if N > 9:
    lst = M[1]
else:
    lst = N
lst = int(lst)
if 10 < N < 20:
    if lst == 0 or lst == 5 or lst == 6 or lst == 7 or lst == 8 or lst == 9:
        print(N, 'korov')
    elif N == 11:
        print(N, 'korova')
    else:
        print(N, 'korovy')
elif N < 10:
    if N == 0 or N == 5 or N == 6 or N == 7 or N == 8 or N == 9:
        print(N, 'korov')
    elif N == 1:
        print(N, 'korova')
    else:
        print(N, 'korovy')
elif lst == 0 or lst == 5 or lst == 6 or lst == 7 or lst == 8 or lst == 9:
    print(N, 'korov')
elif lst == 1:
    print(N, 'korova')
else:
    print(lst)
