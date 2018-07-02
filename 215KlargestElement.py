class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

def main():
	nums = [3,2,3,1,2,4,5,5,6]
	k = 4
	foo = Solution()
	x = foo.findKthLargest(nums, k)
	print(x)

if __name__ == '__main__':
	main()

