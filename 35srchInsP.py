class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        
        if target == nums[len(nums)-1]:
            return len(nums)-1

        if target > nums[-1]:
            return len(nums)

        return self.bisearch(nums, target)

    def bisearch(self, nums, target):
        middle = len(nums)//2
        if target < nums[middle]:
            return self.searchInsert(nums[:middle], target)
        elif target >= nums[middle]:
            return middle + self.searchInsert(nums[middle:], target)

if __name__ == '__main__':
    foo = Solution()
    s = [1,3,5,6]
    input = [3,2,7,0]
    for i in input:
        x = foo.searchInsert(s, i)
        print(x)

