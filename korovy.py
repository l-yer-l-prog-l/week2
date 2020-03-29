N = int(input())
M = str(N)
if 9 < N:
    lst = int(M[1])
    if lst == 0 or lst == 5 or lst == 6 or lst == 7 or lst == 8 or lst == 9:
        print(N, 'korov')
elif 9 < N < 20:
    print(N, 'korov')
elif N == 1:
    print(N, 'korova')
elif N == 0 or N == 5 or N == 6 or N == 7 or N == 8 or N == 9:
    print(N, 'korov')
elif N > 20:
    lst = int(M[1])
    if lst == 1:
        print(N, 'korova')
else:
    print(N, 'korovy')
