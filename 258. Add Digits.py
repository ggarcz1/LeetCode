def addDigits(num):
    sum = num
    # ensure number is greater than 
    while sum >= 10:
        # reset values
        num = sum
        sum = 0
        # add the digits
        while num > 0:
            sum += num % 10 
            num = num / 10
    return sum