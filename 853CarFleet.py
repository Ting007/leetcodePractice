class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = {}
        for i in range(len(position)):
        	dist = target - position[i]
        	tcost = dist/speed[i]
        	time[position[i]] = tcost
        #print(time)
        count = 0
        position.sort()
        #print(position)
        for i in range(len(position)-1, 0, -1):
        	if time[position[i]] > time[position[i-1]]: 
        		time[position[i-1]]= time[position[i]]
        return len(set(time.values()))
        

def main():
	target = 12
	position = [10, 8, 0, 5, 3]
	speed = [2, 4, 2, 1, 3]
	foo = Solution()
	print(foo.carFleet(target, position, speed))

if __name__ == '__main__':
	main()


