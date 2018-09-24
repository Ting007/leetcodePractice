class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num) or num == '0':
        	return '0'
        count = 0
        num1 = num
        for i in range(len(num1)):
        	if count < k:
        		first = num1[:i]+ num1[(i+1):]
        		second = num1[:(i+1)] + num1[(i+2):]
        		if int(first) > int(second):
        			num1 = second
        		else:
        			num1 = first
        		count += 1
        	else:
        		break

        for i in range(len(num)-1, -1, -1):
        	if count < k:
        		first = num[:i] + num[(i+1):]
        		second = num[:(i-1)] + num[i:]
        		if int(first) > int(second):
        			num = second
        		else:
        			num = first
        		count += 1
        	else:
        		break
        return str(min(int(num), int(num1)))

if __name__ == '__main__':
	foo = Solution()
	x = foo.removeKdigits('4321', 2)
	print(x)
        	
