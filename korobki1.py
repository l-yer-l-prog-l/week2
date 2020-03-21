def average(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
short1 = min(a1, b1, c1)
short2 = min(a2, b2, c2)
large1 = max(a1, b1, c1)
large2 = max(a2, b2, c2)
average1 = average(a1, b1, c1)
average2 = average(a2, b2, c2)
if short1 <= short2 and large1 <= large2 and average1 <= average2:
    print('The first box is smaller than the second one')
elif short1 == short2 and large1 == large2 and average1 == average2:
    print('Boxes are equal')
elif short1 >= short2 and large1 >= large2 and average1 >= average2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
