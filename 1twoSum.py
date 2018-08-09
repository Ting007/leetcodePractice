class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=set()
        diff = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index:
                return [i, nums.index(diff)]
            index.add(nums[i])
        return []

            

def main():
        foo = Solution()
        allnums = [[50, 24, 79, 50, 88, 345, 0], [0,0], []]
        target = 100
        for nums in allnums:
            print(foo.twoSum(nums, target))

if __name__ == "__main__":
        main()