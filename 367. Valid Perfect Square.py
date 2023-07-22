def isPerfectSquare(self, num):
    value = 1
    while (value*value <= num):
        if value *value == num:
            return True
        value += 1
        
    return False