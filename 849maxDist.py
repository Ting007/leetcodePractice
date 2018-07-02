import math
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seated = [0]
        dist = []
        for i in range(len(seats)):
        	if seats[i] == 1:
        		seated.append(i)
        seated.append(len(seats)-1)
        for i in range(len(seated)-1):
        	if i == 0 or i == len(seated)-2:
        		dist.append(seated[i+1] - seated[i])
        	else:
        		dist.append(int((seated[i+1]-seated[i])/2))
        return max(dist)

def main():
	foo = Solution()
	s = [[0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1],[1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1]]
	for seats in s:
		print(foo.maxDistToClosest(seats))

if __name__ == '__main__':
	main()



