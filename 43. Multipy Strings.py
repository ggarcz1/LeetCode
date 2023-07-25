def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # define dictionaries 
        str_to_int = {"0": 0,"1": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9}
        int_to_str = {0: "0", 1: "1",2: "2",3: "3",4: "4",5: "5",6: "6",7: "7",8: "8",9: "9"}

        # define two numbers 
        n1 = 0
        n2 = 0
        counter = 0
        # iterate through first number, reversing the number
        for idx in num1[::-1]:
            # build a number
            n1 += str_to_int[idx] * pow(10, counter)
            counter += 1
        counter = 0
        for idx in num2[::-1]:
            n2 += str_to_int[idx] * pow(10, counter)
            counter += 1
        
        # find result
        result = n1*n2
        
        # edge case
        if result == 0:
             return "0"
        final = ""
        
        # rebuild into string
        while result != 0:
            final += int_to_str[result % 10]
            result /= 10

        return final[::-1]