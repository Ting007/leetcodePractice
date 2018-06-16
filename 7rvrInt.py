class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rvr_num = self.strReverse(x)
        if abs(int(rvr_num)) > 2**31-1:
        	return 0
        else:
        	return int(rvr_num)

    def strReverse(self, x):
        temp = str(x)
        output = ""
        if len(temp) == 1:
        	return temp 
        else:
        	if temp[0].isdigit():
        		output=self.strReverse(temp[-1]) + self.strReverse(temp[:-1])
        		return output
        	else:
        		output=temp[0] + self.strReverse(temp[-1]) + self.strReverse(temp[1:-1])
        		return output

def main():
	foo = Solution()
	s = -1230
	print(foo.reverse(s))
	s = 1234567899
	print(foo.reverse(s))

if __name__ == '__main__':
	main()
