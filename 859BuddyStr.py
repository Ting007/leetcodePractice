class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        #first check if AB has the same length and same sets of letters
        if len(A) != len(B) or set(A) != set(B):
        	return False
        #if A == B, we check if the letter are repeated more than once.
        if A == B:
        	for letter in A:
        		if A.count(letter) >1:
        			return True
        # if A not equal to B, find out the index of letter first
        # then compare if swapping works for the equality
        index = []
        for i in range(len(A)):
        	if A[i] != B[i]:
        		index.append(i)
        if len(index) != 2:
        	return False
        return A[index[0]] == B[index[1]] and  A[index[1]] == B[index[0]] 

def main():
	A = "abab"
	B = "abab"
	foo = Solution()
	print(foo.buddyStrings(A, B))

if __name__ == '__main__':
	main()