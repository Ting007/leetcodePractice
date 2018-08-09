class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = set()
        for i in range(len(numbers)):
        	differ = target - numbers[i]
        	if differ in nums1:
        		return [numbers.index(differ), i]
        	nums1.add(numbers[i])
        return[]

if __name__ == '__main__':
	s = [[1,2,3,4], [5,6,7,8], [0, 2, 3, 4, 5], [-7, 0]]
	foo = Solution()
	for i in s:
		x = foo.twoSum(i, 7)
		print(x)
