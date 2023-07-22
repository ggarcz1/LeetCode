def isPalindrome(self, x):
    forward = str(x)
    rev = str(x)[::-1]
    return forward == rev