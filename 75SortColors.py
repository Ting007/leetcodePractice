class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #set two (i, j) pointer, i for 0's, j for 0's and 1's
        i, j = 0, 0
        for k in range(len(nums)):
        	# print(nums)
        	v = nums[k]
        	nums[k] = 2
        	if v < 2:
        		nums[j] = 1
        		j += 1
        	if v == 0:
        		nums[i] = 0
        		i += 1



if __name__ == '__main__':
	s = [0,1,2,1,1,2,0,0,2]
	foo = Solution()
	foo.sortColors(s)