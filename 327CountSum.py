class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        count = 0
        if nums == []:
        	return count

        return self.validSum(nums, lower, upper, count)

        

    def validSum(self, nums, lower, upper, count):
    	if len(nums) == 1:
    		if nums[0] >= lower and nums[0] <= upper:
    			count += 1
    		return count

    	for i in nums:
    		if i <= upper and i >= lower:
    			count += 1
    	for i in range(len(nums)-1):
    		nums[i] += nums[i+1]
    	nums.pop()
    	return self.validSum(nums, lower, upper, count)




if __name__ == '__main__':
	foo = Solution()
	x = foo.countRangeSum([-2, 5, -1], -2, 2)
	print(x)
	x = foo.countRangeSum([2147483647,-2147483648,-1,0], -1, 0)
	print(x)
