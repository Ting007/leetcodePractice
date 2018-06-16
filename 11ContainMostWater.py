class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        container = 0
        left = 0
        right = len(height)-1
        

        while left < right:
        	left_val = height[left]
        	right_val = height[right]
        	if left_val <= right_val:
        		area = left_val*(right-left)
        		left += 1
        		left_next = height[left]
        		while left_next < left_val:
        			left = left+1
        			left_next = height[left]

        	else:
        		area = right_val*(right-left)
        		right -=1
        		right_next = height[right]
        		while right_next < right_val:
        			right = right-1
        			right_next = height[right]

        	if area > container:
        		container = area

        return container

def main():
	input = [1, 2,3,4]
	foo = Solution()
	print(foo.maxArea(input))

if __name__ == '__main__':
	main()