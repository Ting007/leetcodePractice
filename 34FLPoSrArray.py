class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums)-1
        res = [-1, -1]
        while lo <= hi and (res[0] == -1 or res[1]== -1):
        	if target > nums[lo]:
        		lo += 1
        	elif target == nums[lo]:
        		res[0] = lo
        	else:
        		hi = lo -1
        	if target < nums[hi]:
        		hi -= 1
        	elif target == nums[hi]:
        		res[1] = hi
        	else:
        		lo = hi +1
        return res

if __name__ == '__main__':
	nums = [5,7,7,8,8,10]
	foo = Solution()
	x = foo.searchRange(nums, 6)
	print(x)
	



