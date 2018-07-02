class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sValue={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        i = 0
        while i < len(s):
        	if i < (len(s) - 1) and sValue[s[i]] < sValue[s[i+1]]:
        		total = total - sValue[s[i]]+sValue[s[i+1]]
        		i += 2
        	else:
        		total += sValue[s[i]]
        		i+=1
        return total

def main():
	s = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
	foo=Solution()
	for each in s:
		print(foo.romanToInt(each))

if __name__ == '__main__':
	main()


