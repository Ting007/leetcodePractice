import cProfile
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        if len(set(nums))==1 and nums[0] == 1:
            return len(nums)
        jumplen = [0]*(len(nums))
        counter = 1
        for i in range(len(nums)):
            jumplen[i] = nums[i]+i
        if jumplen[0]>= len(nums)-1:
            return counter
        else:
            return self.selectJump(len(nums), jumplen, counter+1, 0)



    def selectJump(self, gap, jumplen, counter, start):
        # if jumplen[0] >= gap-1:
        #     return counter+1 
        # else:
        maxjump = max(jumplen[start+1:(jumplen[start]+1)])
        start = jumplen.index(maxjump)
        if maxjump >= gap-1:
            return counter 
        return self.selectJump(gap, jumplen, counter+1, start)



if __name__ == '__main__':
    foo = Solution()
    sample = [[2,3,1,1,4], [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3], [2,3,0,1,4], [1,2], [1,2,3], [1,1,1,1,1]]
    for s in sample:
        cProfile.run("foo.jump(s)")
        # print(x)


