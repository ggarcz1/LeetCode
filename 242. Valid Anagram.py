class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # compare counts of each character
        # in each string 
        if len(s) != len(t):
            return False

        # define empty hashmaps
        s_string = {}
        t_string = {}
        
        # iterate through the first string, 's'
        for value in s:
            if s_string.get(value) is not None:
                # increment if value exists
                s_string[value] = s_string.get(value) + 1
            elif s_string.get(value) is None:
                # set value to 1 if DNE
                s_string[value] = 1
        
        # iterate trhough the second string, 't
        for value in t:
            if t_string.get(value) is not None:
                # increment if value exists
                t_string[value] = t_string[value] + 1
            elif t_string.get(value) is None:
                # set value to 1 if DNE
                t_string[value] = 1

        # run through first hashmap
        for idx in s_string:
            # if the string DNE in t hashmap, return false
            if t_string.get(idx) is None:
                return False
            # if the count is not correct, return false
            if s_string[idx] != t_string[idx]:
                return False

        return True 
        # this may also work
        # return s_string == t_string     