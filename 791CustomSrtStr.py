class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order = {}
        extra = ''
        for i in S:
        	order[i] = 0
        for j in T:
        	if j in S:
        		order[j] += 1
        	else:
        		extra += j
        for i in S:
        	extra += i*order[i]
        return extra

if __name__ == '__main__':
	a = "cba"
	b = "acdb"
	foo = Solution()
	x = foo.customSortString(a, b)
	print(x)
