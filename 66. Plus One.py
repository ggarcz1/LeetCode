def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    re_digits = []
    value = 0
    counter = 0
    digits.reverse()
    for idx in digits:
        value += idx * pow(10, counter)
        counter += 1
    value+=1
        
    while value > 0:
        re_digits.insert(0, value % 10)
        value = value / 10

    return re_digits