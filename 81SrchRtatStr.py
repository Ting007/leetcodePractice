class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = len(nums)-1
        for i in range(len(nums)-1):
        	if nums[i] > nums[i+1]:
        		pivot = i
        if nums == [] or target > nums[pivot] or target < nums[(pivot+1)%len(nums)]:
        	return False

        if target >= nums[0]:
        	l = 0
        	r = pivot
        	return self.binarySearch(target, nums, l, r)
        elif target < nums[0]:
        	l = pivot+1
        	r = len(nums)-1
        	return self.binarySearch(target, nums, l, r)
        

    def binarySearch(self, target, nums, l, r):
    	"""
    	:type nums: List[int]
    	:type target: int
    	:rtyep: int (index of target in the nums)
    	"""
    	if target > nums[r] or target < nums[l]:
    		return False
    	mid = int((l+r)/2)
    	if target > nums[mid]:
    		return self.binarySearch(target, nums, mid+1, r)
    	elif target < nums[mid]:
    		return self.binarySearch(target, nums, l, mid-1)
    	elif target == nums[mid]:
    		return True

if __name__ == '__main__':
	nums = [4,5,6,7,0,0,1,2]
	nums = [4,5,6,7,0,1,2,3]
	target = 0
	foo = Solution()
	x = foo.search(nums, target)
	print(x)

