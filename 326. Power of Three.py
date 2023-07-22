def isPowerOfThree(self, n):
    """
    :type n: int
    :rtype: bool
    """
    #edge case
    if n < 1 or n == 2:
        return False
    while n > 1:
        if n%3 != 0:
            return False
        n=n/3
    return True