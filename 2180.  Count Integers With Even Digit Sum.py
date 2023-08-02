def countEven(self, num):
    """
    :type num: int
    :rtype: int
    """
    counter = 0
    # add digits
    for idx in range(1, num+1):
        sum = 0
        while idx > 0:
            # mod  gets the value to add
            sum += idx % 10 
            # divide pops off the remainder
            idx = idx / 10
        if sum % 2 == 0:
            counter+=1

    return counter