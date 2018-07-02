class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        topK = []
        for i in nums:
        	if i in freq.keys():
        		freq[i] += 1;
        	else:
        		freq[i] = 1
        ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # print(ordered)
        for i in range(k):
        	topK.append(ordered[i][0])
        return topK


def main():
	foo=Solution()
	a = foo.topKFrequent([1,1,1,2,2,3], 2)
	print(a)

if __name__ == '__main__':
	main()

