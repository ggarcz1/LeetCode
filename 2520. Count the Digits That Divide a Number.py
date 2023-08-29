class Solution:
    def countDigits(self, num: int) -> int:
        arr = [*str(num)]
        counter = 0
        for idx in arr:
            if num % int(idx) == 0:
                counter+=1
        return counter