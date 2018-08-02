import bisect
class Solution:
    def kEmptySlot(self, flowers, k):
        active = []
        for day, value in enumerate(flowers, 1):
            i = bisect.bisect(active, value)
            if i > 0 and (abs(value-active[i-1]) == k or abs(active[i+1] - value) == k):
                return day
            active.insert(i, value)
        return -1



        # active = []
        # for day, flower in enumerate(flowers, 1):
        #     print(active, flower)
        #     i = bisect.bisect(active, flower)
        #     for neighbor in active[i-(i>0):i+1]:
        #         if abs(neighbor - flower) - 1 == k:
        #             return day
        #     active.insert(i, flower)
        # return -1






def main():
	f = [2,4,5,3,1,8,7,6]
	foo = Solution()
	x = foo.kEmptySlot(f, 2)
	print(x)

if __name__ == '__main__':
	main()
