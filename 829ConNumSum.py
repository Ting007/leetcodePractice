class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        k = 1
        while k < (2*N)**(1/2):
        	if (N-k*(k-1)/2)%k == 0:
        		count += 1
        	k += 1
        return count

if __name__ == '__main__':
	foo = Solution()
	x = foo.consecutiveNumbersSum(9)
	print(x)
