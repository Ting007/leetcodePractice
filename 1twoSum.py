class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index={}
        output=[]
        diff = 0
        for i, num in enumerate(nums):
        #	if num <= target:
        	index[i]=num
  
        for i, num in index.items():
        	diff = target - num
        	#print(diff)
        	for j in index.keys():
	        		if index[j] == diff and j > i:
	        			output.append(i)
        				output.append(j)
        return output

def main():
        foo = Solution()
        nums = [-50, 24, 79, 50, 88, 345, 0]
        target = 0
        print(foo.twoSum(nums, target))

if __name__ == "__main__":
        main()