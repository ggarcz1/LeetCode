class Solution(object):
    def reverse(self, x):
        # 0 edge case
        if x == 0:
            return x
        
        #check for negative value and set flag
        neg = False
        if x < 0:
            neg = True
            x *= -1

        value = 0
        counter = 0
        arr = []
        # iterate through the input and append to arr
        while x > 0:
            arr.append(x%10)
            x= int(x/10)
        # reverse the array and iterate 
        for idx in arr[::-1]:
            # rebuild the string with * 10 values
            value = value + idx * pow(10, counter)
            counter += 1
        #check for negative
        if neg: 
            value = (value *-1)
            #check for out of bounds range
            if value < pow(-2,31):
                return 0

        #check for out of bounds range
        if value > pow(2,31)-1:
            return 0

        return value