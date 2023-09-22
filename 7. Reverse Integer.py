class Solution(object):
    def reverse(self, x):
        if x == 0:
            return x
        neg = False
        if x < 0:
            neg = True
            x *= -1

        value = 0
        counter = 0
        arr = []
        while x > 0:
            arr.append(x%10)
            x= int(x/10)
        for idx in arr[::-1]:
            # if counter == 1:
            value = value + idx * pow(10, counter)
            counter += 1
        if neg: 
            value = (value *-1)
            if value < pow(-2,31):
                return 0

        if value > pow(2,31)-1:
            return 0

        return value