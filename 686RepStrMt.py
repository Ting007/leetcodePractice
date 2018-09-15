class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sub = A
        i = 1
        while len(A) <= (len(B)+2*len(sub)):
        	# print(A, B)
        	if B in A:
        		return i
        	else:
        		A += sub
        		i += 1
        return -1





if __name__ == '__main__':
	A = ["aabb", "aabbc", "abc", "abcabcabcabc"]
	B = ["ba", "bca", "cabcabca", "abac"]
	foo = Solution()
	for a,b in zip(A,B):
		x = foo.repeatedStringMatch(a, b)
		print(x)