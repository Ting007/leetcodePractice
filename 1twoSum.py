class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index={}
        diff = 0
        for i, num in enumerate(nums):
        #	if num <= target:
        	index[num]=i
        for i in range(len(nums)):
        	diff = target - nums[i]
        	if diff in index and index[i] != i:
        		return [i, index[diff]]
            

def main():
        foo = Solution()
        nums = [50, 24, 79, 50, 88, 345, 0]
        target = 100
        print(foo.twoSum(nums, target))

if __name__ == "__main__":
        main()