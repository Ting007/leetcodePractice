class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
        	return s
        repeat = 2+2*(numRows-2)
        s2 = ["" for i in range(numRows)]
        for i in range(len(s)):
        	temp = i%repeat
        	if temp < numRows:
        		s2[temp]+=s[i]
        	else:
	        	s2[repeat-temp]+=s[i]
        return "".join(s2)




def main():
        foo = Solution()
        s="paypalishiring"
        print(foo.convert(s, 4))

if __name__ == "__main__":
        main()