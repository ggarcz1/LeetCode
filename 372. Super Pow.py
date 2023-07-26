def superPow(self, a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    num = ''
    for idx in b:
        num += str(idx)
    num = int(num)

    return pow(a, num, 1337)

