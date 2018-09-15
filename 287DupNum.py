class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast =  nums[0], nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # # print(slow, fast)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow

if __name__ == '__main__':
    s = [1,3,4,2,2]
    foo = Solution()
    foo.findDuplicate(s)