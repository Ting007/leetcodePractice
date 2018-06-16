class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        
        while (left < right and height[left] <= height[left+1]):
        	left += 1
        while (right > left and height[right] <= height[right-1]):
        	right -= 1

        maxLeft = height[left]
        maxRight = height[right]
        area = 0

        while left <= right:
        	#Here if left is smaller than right
        	# then the left side is the limit
        	#filling from the top right to the left bottom
        	if maxLeft < maxRight:
        		if height[left] > maxLeft:
        			maxLeft = height[left]
        			left += 1
        		else:
        			area += maxLeft-height[left]
        			left += 1
        	else:
        		if height[right] > maxRight:
        			maxRight = height[right]
        			right-=1
        		else:
        			area += maxRight-height[right]
        			right -= 1
        return area



def main():
	s = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
	foo = Solution()
	print(foo.trap(s))

	s = [5,5,1,7,1,1,5,2,7,6]
	foo = Solution()
	print(foo.trap(s))

if __name__ == '__main__':
	main()