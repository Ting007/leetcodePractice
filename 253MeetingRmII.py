import bisect
class Solution():
	def meetingRoom(self, times):
		"""
		:type: times: list[list[int]]
		:rtype: int
		"""
		if S == [[]]:
			return 0
		times.sort(key=lambda r:r[0])
		meet = times[0]
		room = 1
		for i in range(1, len(times)):
			insertP1 = bisect.bisect(meet, times[i][0])
			insertP2 = bisect.bisect(meet, times[i][1])
			if insertP1 > 0 and insertP2 < len(meet) and insertP1 == insertP2:
				room = len(meet) - insertP1+1
				# print(meet, insertP1)
			meet.insert(insertP1, times[i][0])
			insertP2 = bisect.bisect(meet, times[i][1])
			meet.insert(insertP2, times[i][1])
		return room

if __name__ == '__main__':
	S = [[5,6], [10, 15], [3,4]]#, [3,7]] #[3,7], [2,6], [10, 15],
	# S = [[0, 30], [5, 10], [15, 20], [16, 19]]
	foo = Solution()
	x = foo.meetingRoom(S)
	print(x)



