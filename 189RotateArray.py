class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6,7]
        [5,6,7,1,2,3,4]
        """
        k = k%len(nums)
        self.reverse(nums, len(nums)-1, 0)
        self.reverse(nums, len(nums)-1, k)
        self.reverse(nums, k-1, 0)
        return nums
        """
        length = len(nums)
        k = k % length
        nums[:k], nums[k:] = nums[length-k:], nums[:length-k]
        """


    def reverse(self, nums, r, l):
    	"""
    	:type nums: List[int]
    	:type r : int # the right cursor of the array
    	:tyep l : int # the left cursor of the array
    	the main purpose it to invert the array between r and l
    	[1,2,3,4] => [4,3,2,1]
    	"""
    	while r > l:
    		temp = nums[r]
    		nums[r] = nums[l]
    		nums[l] = temp
    		r -= 1
    		l += 1



def main():
	foo = Solution()
	s = [1,2,3,4,5,6,7]
	# s = [-1, -100, 3, 99]
	s = [2]
	x = foo.rotate(s, 3)
	print(x)

if __name__ == '__main__':
	main()
