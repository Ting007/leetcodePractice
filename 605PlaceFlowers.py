class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
        	return True
        i = 1
        flowerbed = [0] + flowerbed+[0]
        while i < len(flowerbed)-1:
        	if flowerbed[i] == 0:
        		if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        			n -= 1
        			flowerbed[i] = 1
        			i += 2
        		else:
        			i+= 1
        	else:
        		i+=1
        	if n == 0:
        		return True
        	
        return False

        	


        	

if __name__ == '__main__':
	fl = [[0,0,0,0,0,1,0,0], [1,0,0,0,1], [0,0,1,0,0,0,1], [1, 0]]
	foo = Solution()
	for f in fl:
		x = foo.canPlaceFlowers(f, 1)
		print(x)

		