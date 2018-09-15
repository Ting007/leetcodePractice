class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
        	return len(nums)
        n = 2
        i = 2
        while i < len(nums):
        	if nums[i] != nums[n-2]:
        		nums[n]= nums[i]
        		i += 1
        		n += 1
        	else:
        		i += 1
        		# nums[i] = nums[n]
        return n

if __name__ == '__main__':
	nums = [[1,1,1,2,2,3],[0, 0, 1, 1, 1, 2, 3, 3], [2,2,1,1,1,3,3]]
	foo = Solution()
	for s in nums:
		foo.removeDuplicates(s)
