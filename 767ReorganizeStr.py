import collections
import math
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        r_str = ''
        c = collections.Counter(S)
        if c.most_common(1)[0][1] > math.ceil(len(S)/2):
        	return ''
        while len(r_str) < len(S):
        	a = c.most_common(2)
        	for i in a:
        		if r_str == '' or r_str[-1] != i[0]:
        			r_str += i[0]
        			c[r_str[-1]] -= 1
        			break
        return r_str

if __name__ == '__main__':
	S = ["aab", "aaabbdc", "aaab", "baaba"]
	foo = Solution()
	for i in S:
		x = foo.reorganizeString(i)
		print(x)

        

