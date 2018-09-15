class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gap = 0
        for i in range(len(nums)-1):
        	gap = max(gap, (nums[i] + i))
        	if nums[i] == 0:
        		if gap <= i :
        			return False

        if gap >= len(nums)-1:
        	return True

def main():
	S = [[2,3,1,1,4], [3,2,1,0,4], [4,1,0,1,2,2,0,0],[2,3,1,0,2,4,0,0,5], [0,0,0,3,1]]
	foo = Solution()
	for i in S:
		x = foo.canJump(i)
		print(x)

if __name__ == '__main__':
	main()

