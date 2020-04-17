def natural(nat):
    i = 2
    count = 0
    while nat % i != 0:
        i += 1
        count += 1
    return i
nat = int(input())
print(natural(nat))
