class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        medium = nums[len(nums)//2]
        return sum([abs(medium-num) for num in nums])