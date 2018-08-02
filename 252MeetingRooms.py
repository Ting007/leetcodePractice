import bisect
class Solution:
	def attendMeetings(self, times):
		"""
		:type: List[list[int]]
		:rtype: boolean
		"""
		if times == [[]]:
			return True
		times.sort(key=lambda r :r[0])
		#set the first meeting time
		meet = times[0]
		#iterate through all the times
		for i in range(1, len(times)):
			#find inserting point in the meet time
			for time in times[i]:
				insertP = bisect.bisect(meet, time)
				#if the inserting happened at the middle of the sequence
				print(meet, insertP, time, len(meet))
				if insertP > 0 and insertP < len(meet):
					# there will be a conflicts
					return False
				meet.insert(insertP, time)
					# meet.sort()
		return True

if __name__ == '__main__':
	S = [[5,6], [10, 15], [3,4]] #[3,7], [2,6], [10, 15],
	# S = [[]]
	S = [[0, 30], [5, 10], [15, 20]]
	foo = Solution()
	x = foo.attendMeetings(S)
	print(x)

