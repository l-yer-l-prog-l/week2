a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    if a <= b and b < c:
        print(a, b, c)
    elif a < b and c <= b:
        print(a, c, b)
elif b <= a and b <= c:
    if b <= a and a < c:
        print(b, a, c)
    elif b < a and c <= a:
        print(b, c, a)
elif c <= a and c <= b:
    if c <= a and a < b:
        print(c, a, b)
    elif c < a and b <= a:
        print(c, b, a)
else:
    print()
