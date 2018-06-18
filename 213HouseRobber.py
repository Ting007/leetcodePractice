class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
        	return 0
        if len(nums) < 4:
        	return max(nums)
        fragment1 = nums[:-1]
        fragment2 = nums[1:]
        # print(fragment1, fragment2)
        part1 = self.robMax(fragment1)
        part2 = self.robMax(fragment2)
        return max(part1, part2)

    def robMax(self, nums):
    	odd = 0
    	even = 0
    	for i in range(len(nums)):
    		if i%2 == 1:
    			odd = max(even, nums[i]+ odd)
    		else:
    			even = max(odd, nums[i]+even)
    	return max(odd, even)

def main():
	foo = Solution()
	s = [[2,3,2],[1,2,3,1],[3,4,5,1,2]]
	for item in s:
		print(foo.rob(item))

if __name__ == '__main__':
	main()
