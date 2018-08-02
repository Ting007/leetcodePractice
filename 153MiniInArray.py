class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = len(nums)-1
        for i in range(len(nums)-1):
        	if nums[i] > nums[i+1]:
        		pivot = i
        return nums[(pivot+1)%len(nums)]