class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-min(nums)*len(nums)

if __name__ == '__main__':
	foo = Solution()
	x = foo.minMoves([1,2,3])
	print(x)
