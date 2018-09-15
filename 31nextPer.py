class Solution:
	def nextPermutation(self, nums):
		"""
		:type nums: list[int]
		:rtyep: void not return anything modify nums
		"""
		i = len(nums)-1
		index = 0

		while i >= 0:
			j = self.modify(nums, i)
			if j != i:
				temp = nums[j]
				nums[j] = nums[i]
				nums[i] = temp
				index = j
				break
			i = i -1
		nums[(i+1):] = sorted(nums[(i+1):])


	def modify(self, nums, i):
		control = nums[i]
		index = i
		temp = max(nums)
		for j in range(i+1, len(nums)):
			if control < nums[j] and temp >= nums[j]:
				temp = nums[j]
				index = j
		return index


if __name__ == '__main__':
	foo = Solution()
	s = [[1,3,2], [3,2,1], [1,1,5], [2,4,3,5,1], [3,4,5,2,1], [4,2,0,2,3,2,0]]
	for a in s:
		foo.nextPermutation(a)