X = float(input())
Y = float(input())
tenpercent = X / 10
count = 1
while X < Y:
    tenpercent = X / 10
    X = X + tenpercent
    count += 1
print(count)
