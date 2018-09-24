class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, [], 0)
        return res
        
    def dfs (self, candidates, target, res, path, index):
        if target == 0:
            res.append(path)
        elif target < 0:
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] <= target:
                    self.dfs(candidates, target-candidates[i], res, path+[candidates[i]], i)




if __name__ == '__main__':
	foo = Solution()
	foo.combinationSum([2,3,5,8], 8)
	s = 123
	x = foo.combinationSum([2,3,5], 8)
	print(x)