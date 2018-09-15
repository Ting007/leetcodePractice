import collections
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        degree = max(c.values())
        m = collections.defaultdict(list)
        for i in range(len(nums)):
        	m[nums[i]].append(i)
        return min(m[k][-1]-m[k][0]+1 for k in m.keys() if c[k] == degree)






if __name__ == '__main__':
	foo = Solution()
	s = [1,2,2,3,1]
	# s = [1,2,2,3,1,1,4,2]
	s = [1,1,2,2,2,1]
	x = foo.findShortestSubArray(s)
	print(x)

        	