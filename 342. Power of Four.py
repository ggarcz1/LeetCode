def isPowerOfFour(self, n):
    """
    :type n: int
    :rtype: bool
    """
    #edge case
    if n < 1 or n == 3:
        return False
    
    while n > 1:
        if n%4 != 0:
            return False
        n=n/4

    return True