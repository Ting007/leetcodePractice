class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if target == 0:
        	return [[]]
        if target in candidates:
        	res.append([target])
        for i in range(len(candidates)):
        	temp = []
        	if candidates[i] >= target:
        		break
        	else:
        		target -= candidates[i]
        		temp = self.combinationSum(candidates[1:], target)
        		if temp:
        			temp.append(candidates[i])

        	res.append(temp)
        return res


if __name__ == '__main__':
	foo = Solution()
	x = foo.combinationSum([2,3,5,8], 8)
	print(x)