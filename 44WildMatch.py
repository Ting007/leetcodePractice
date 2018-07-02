import time
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "*" or s == p:
        	return True
        if p == '' or s == '':
        	return False
        if (p.count('?') > len(s)):
        	return False

        result = [[False]*(len(s)+1)for _ in range(len(p)+1)]
        result[0][0] = True

        for i in range(len(p)):
        	if p[i] == "*":
        		result[i+1][0] = True
        	else:
        		break

        for i in range(1, len(p)+1):
        	for j in range(1, len(s)+1):
        		if p[i-1] != "*":
        			result[i][j] = result[i-1][j-1] and\
        		 (s[j-1] == p[i-1] or p[i-1] == '?')
        		else:
        		 	result[i][j] = (result[i-1][j-1] or result[i][j-1] or result[i-1][j])
        for i in result:
        	print(i)
        return result[-1][-1]
        


def main():
	foo = Solution()
	s = "aaaa"
	p = "***a"
	s = "abefcdgiescdfimde"
	p = "ab*cd?i*de"
	# s = "sissippi"
	# p = "*ss*?i*pi"
	# s = "b"
	# p = "*?*?"
	s = "adceb"
	p = "*a*b"
	# s = "a"
	# p = "a*"
	s = "zacabz"
	p = "*a?b*"
	x = foo.isMatch(s, p)
	print(x)

if __name__ == '__main__':
	main()