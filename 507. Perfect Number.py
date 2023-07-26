def checkPerfectNumber(self, num):
    """
    :type num: int
    :rtype: bool
    """
    #edge case
    if num <= 1:
        return False
    total = 1
    counter = 2
    # squareroot
    while counter <= sqrt(num):
        # search for no remainder (divisor)
        if num % counter == 0:
            # add to total, divisor + (divisor*?) aka num/counter = ?
            total += counter + num/counter
            counter += 1

    return (total == num) 