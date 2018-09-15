class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        
    def splitArray2(self, nums):
        """
        :type nums: List[int]
        :type m: int m == 2
        :rtype: int
        split array into 2 subarray
        """
        index = len(nums)//2
        left = nums[:index]
        right = nums[index:]
        l_sum = max(sum(right), sum(left))
        while sum(right) > sum(left):
            index = index + len(right)//2
            left = nums[:index]
            right = nums[index:]
