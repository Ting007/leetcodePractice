class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = [1000, 500, 100, 50, 10, 5, 1]
        sValue={1:'I', 5:'V', 10:'X',50:'L',100:'C',500:'D',1000:'M'}
        result = ""
        digit = []

        for i in range(len(s)):
            divide= int(num/s[i])
            num = num%s[i]
            digit.append(divide)
        # print(digit)

        for i in range(len(digit)-1, -1, -1):
            if digit[i] == 4:
                if i >0 and digit[i-1] ==1:
                    result = sValue[s[i]]+sValue[s[i-2]] + result
                    digit[i] = 0
                    digit[i-1] = 0
                else:
                    result = sValue[s[i]] + sValue[s[i-1]] + result
                    digit[i] = 0
            else:
                while digit[i] > 0:
                    result = sValue[s[i]] + result
                    digit[i] -= 1 
            
        return result


def main():
	foo = Solution()
	s = [3, 4, 9, 58, 1994]
	for num in s:
		print(foo.intToRoman(num))

if __name__ == '__main__':
	main()