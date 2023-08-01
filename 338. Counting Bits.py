def countBits(n):
    lst = []
    for idx in range(0, n+1):
        num = idx
        counter = 0
        while num > 0:
            counter += num & 1
            num = num >> 1
        lst.append(counter)

    return lst