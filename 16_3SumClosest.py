class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
        	return None
        if len(nums) == 3:
        	return sum(nums)

        nums.sort()
        total = sum(nums[:3])
        closest = abs(total- target)
        dist = list(set(nums)) # eliminate the duplicates
        for x in range(len(dist)):
        	i = nums.index(dist[x])+1
        	j = len(nums)-1
        	while i < j:
        		b = nums[i]+nums[j]+dist[x]
        		temp = abs(b-target)
        		# print(nums, nums[i], nums[j], dist[x])
        		if temp < closest:
        			# print("smaller than")
        			# print(nums, nums[i], nums[j], dist[x])
        			total = b
        			closest = temp
        		if b > target:
        			j -= 1
        		elif b < target:
        			i += 1
        		else:
        			return b

        return total

def main():
	foo = Solution()
	s = [-1,1, 2, -4]
	# s = [1,2,4,8,16,32,64,128]
	print(foo.threeSumClosest(s, 82))

if __name__ == '__main__':
	main()
