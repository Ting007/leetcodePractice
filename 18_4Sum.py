import collections
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.NSum(nums, target, 4)
        
    def NSum(self, nums, target, N):
    	if len(nums) < N:
    		return []
    	nums.sort()
    	if target < nums[0]* N or target > nums[-1]* N:
    		return []
    	if N == 2:
    		return self.twoSum(nums, target)
    	else:
    		result = []
    		for i in range(len(nums)-N+1):
    			if i > 0 and nums[i] == nums[i-1]:
    				continue
    			else:
    				subresult = self.NSum(nums[(i+1):], (target-nums[i]), N-1)
    				if subresult != []:
    					for subR in subresult:
    						subR.append(nums[i])
    				result.extend(subresult)
    		return result

    def twoSum(self, nums, target):
    	A = set()
    	result = []
    	nums.sort()
    	for i in range(len(nums)):
    		if i > 1 and nums[i] == nums[i-2]:
    			continue
    		else:
    			differ = target - nums[i]
    			if differ in A:
    				if result and result[-1] == [differ, nums[i]]:
    					continue
    				result.append([differ, nums[i]])
    			else:
    				A.add(nums[i])
    			# print(nums[i], differ, A)
    	return result








        # nums.sort()
        # if target > 4*nums[-1] or target < 4*nums[0]:
        # 	return []
        
        # sumList = set()
        # A = collections.defaultdict(int)
        # for i in range(len(nums)-1):
        # 	for j in range(i+1, len(nums)):
        # 		sum2 = nums[i] + nums[j]
        # 		A[i, j]=sum2
        # extra = set()
        # for m in A.keys():
        # 	for n in A.keys():
        # 		if m != n and target == A[m]+A[n] and len(set(n).intersection(set(m))) == 0:
        # 			sumList.add((nums[m[0]], nums[m[1]], nums[n[0]], nums[n[1]]))
        # result = []
        # for sublist in sumList:
        # 	sub = list(sublist)
        # 	sub.sort()
        # 	if sub not in result:
        # 		result.append(sub)
        # return result


if __name__ == '__main__':
	S = [[5,5,3,5,1,-5,1,-2], [1, 0, -1, 0, -2, 2], [1, 2, 3, 4, -1, -2, -3, -4], [0,0,0,0], [0,0,0]]
	# S.append([-500,-481,-480,-469,-437,-423,-408,-403,-397,-381,-379,-377,-353,-347,-337,-327,-313,-307,-299,-278,-265,-258,-235,-227,-225,-193,-192,-177,-176,-173,-170,-164,-162,-157,-147,-118,-115,-83,-64,-46,-36,-35,-11,0,0,33,40,51,54,74,93,101,104,105,112,112,116,129,133,146,152,157,158,166,177,183,186,220,263,273,320,328,332,356,357,363,372,397,399,420,422,429,433,451,464,484,485,498,499])
	target = [4, 0, 0, 0, 0]# 2139, 864]
	# S.append([-500,-495,-489,-472,-466,-449,-439,-435,-435,-413,-406,-381,-369,-353,-335,-311,-306,-260,-258,-231,-205,-189,-180,-165,-165,-164,-146,-141,-126,-121,-116,-100,-83,-23,-17,18,53,65,91,124,139,140,164,168,200,202,211,216,221,224,249,251,280,282,300,314,323,348,355,373,401,416,428,443,443,445,462,491,497])
	foo = Solution()
	for i in range(len(S)):
		x = foo.fourSum(S[i], target[i])
		print(x)

