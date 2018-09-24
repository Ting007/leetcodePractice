from heapq import heappush, heappop
class Solution(object):
	def KSort(self, nums, k):
		heap = []
		for item in nums:
			heappush(heap, item)
		order = []
		while heap:
			order.append(heappop(heap))
		return order

if __name__ == '__main__':
	foo = Solution()
	nums = [1,3,5,7,9,6,8,0]
	x = foo.KSort(nums, 2)
	print(x)

		