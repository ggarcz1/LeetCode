def separateDigits(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lst = []
    sum = 0
    # iterate through the provided list
    for idx in nums:
        # if the value is > 10 (aka more than one digit)
        if idx >= 10:
            vals = []
           # break up the number and add to a new list
            while idx > 0:
                # mod  gets the value to add
                digit = int(idx % 10)
                vals.append(digit)
                # divide pops off the remainder
                idx = idx / 10
            # reverse list and add to return list
            for integer in vals[::-1]:
                lst.append(integer)
        else:
            # value is 1 digit, < 10, add to return list
            lst.append(idx)
           
    return lst