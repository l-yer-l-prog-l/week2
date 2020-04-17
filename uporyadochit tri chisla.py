a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    if a <= b and b < c:
        a, b, c = a, b, c
    elif a < b and c <= b:
        a, c, b = a, b, c
elif b <= a and b <= c:
    if b <= a and a < c:
        a, b, c = b, a, c
    elif b < a and c <= a:
        a, b, c = b, c, a
elif c <= a and c <= b:
    if c <= a and a < b:
        a, b, c = c, a, b
    elif c < a and b <= a:
        a, b, c = c, b, a
print(a, b, c)
