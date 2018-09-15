class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
        	return 0
        counter = 0
        for i in range(1, len(nums)):
        	if nums[counter]!= nums[i]:
        		nums[counter+1] = nums[i]
        		counter += 1
        return counter+1