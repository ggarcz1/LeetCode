def mySqrt(self, x):
    """
    :type x: int    
    :rtype: int
    """
    value = 1
    while (value*value <= x):
        value += 1
        
    return int(value-1)