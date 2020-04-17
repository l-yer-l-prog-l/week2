def median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
minabc = min(a, b, c)
medianabc = median(a, b, c)
minde = min(d, e)
maxde = max(d, e)
if minabc <= minde and medianabc <= maxde:
    print("YES")
else:
    print("NO")
