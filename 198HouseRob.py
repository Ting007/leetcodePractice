class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total1 = 0
        total2 = 0
        for i in range(len(nums)):
        	if i%2 == 0:
	        	total1 = max(nums[i]+total1, total2)
	        else:
	        	total2 = max(total1, nums[i]+total2)
	        print(total1, total2)

        return max(total1, total2)




def main():
	foo=Solution()
	s = [[1,2,3,1], [2,7,9,3,1], [2,1,1,2],[2, 1, 1, 2, 3, 4, 2,]]
	for frag in s:
		print(foo.rob(frag))

if __name__ == '__main__':
	main()
