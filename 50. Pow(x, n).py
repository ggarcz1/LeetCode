def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    value = 1
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        if n > 0:
            while n != 0:
                value = value * x 
                n = n - 1
        else:
            while n != 0:
                value = value * x 
                n = n + 1
            value = 1/value
    return value