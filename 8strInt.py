class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "" or str == "+" or str =="-":
        	return 0

        result = self.convert(str)
        if result == '' or (len(result) == 1 and (result == "+" or result =="-")):
        	return 0
        elif len(result) >1 and (not result[1:].isdigit()):
        	return 0
        else:
        	digit = int(result)
        if digit > 2**31-1:
        	return 2**31-1
        if digit < -2**31:
        	return -2**31
        return digit
        

    def convert(self, str):
        digit = ''
        for char in str:
        	if char != ' ':
        		if (len(digit) == 0 and (char == '+' or char == '-')) or char.isdigit():
        			digit += char
        		elif (digit == '+' or digit == '-' or digit=='') and not char.isdigit():
        			return '0'
        		elif (not char.isdigit() and digit[-1].isdigit()):
        			return digit
        	if char == ' ':
        		if len(digit)>0:
        			return digit
        return digit


def main():
	foo=Solution()
	s = ["42", " ", " +-42", "abc123", "-abc123", "   -123  abc", "  -4222abc789 ", "-98334376539", "-", "+", "3.14", " +234 456"]
	for test in s:
		print(foo.myAtoi(test))

if __name__ == '__main__':
	main()
