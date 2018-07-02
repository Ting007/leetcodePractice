class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:
        	return 0
        n = len(heights)
        if n == 1:
        	return heights[0]
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(n+1):
        	while heights[i] < heights[stack[-1]]:
        		h = heights[stack.pop(-1)]
        		w = i - stack[-1]-1
        		ans = max(ans, h*w)
        		# print(h, w, stack)
        	stack.append(i)
        return ans

def main():
	foo = Solution()
	heights = [2,1,5,6,2,3]
	a = foo.largestRectangleArea(heights)
	print(a)

if __name__ == '__main__':
	main()

