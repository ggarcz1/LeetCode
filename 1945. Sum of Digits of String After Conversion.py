def getLucky(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # transform to string number
    num = ''
    for idx in s:
        num += str(ord(idx)-96)
    # add the digits
    sum = 0
    counter = 0
    # convert back to integer
    num = int(num)
    # perfrom iterations, counting up to k, could also do 
    # while k > 0: and k -= 1
    while counter < k: 
        sum = 0
        # add digits
        while num > 0:
            # mod  gets the value to add
            sum += num % 10 
            # divide pops off the remainder
            num = num / 10
        counter += 1
        # set the number to the new value 
        num = sum
    return sum